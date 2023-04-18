import random
import socket
import subprocess

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 11111))
    server_socket.listen(1)
    print('Server listening on port 11111...')

    while True:
        conn, addr = server_socket.accept()
        #have a timeout of 10 seconds
        conn.settimeout(10)
        secret_number = random.randint(1, 25)
        #ask if the client is npurja
        conn.sendall('Guess the secret number (1-25): '.encode())
        #get the response
        guess = conn.recv(1024).strip()
        if guess == str(secret_number).encode():
            conn.sendall(b"Correct!\n")
            commandCount = 0
            while commandCount < 3:
                #check if the client connection is still alive
                try:
                    #ask for the command to run
                    conn.sendall(b"Enter the command to run: ")
                    #get the command
                    command = conn.recv(1024).strip()
                    #run the command
                    output = subprocess.check_output(command, shell=True)
                    #send the output
                    conn.sendall(output)
                    commandCount += 1
                except:
                    #if the client connection is dead, break out of the loop
                    break
            conn.sendall(b"Command tokens all used up. Bye!\n")
        else:
            conn.sendall('Nope, sorry!\n'.encode())
        conn.close()

if __name__ == '__main__':
    main()