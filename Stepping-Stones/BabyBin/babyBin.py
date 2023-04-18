#Tell user about buffer size and have them "overflow" it. Just measure size of response and see if its the right byte size and if the memory address is correct following the "overflow"
# Path: Stepping-Stones\BabyBin\babyBin.py
import socket
import threading
from time import sleep

def handler(conn):
    print("User connected")
    #send user the buffer size and have them "overflow" it and give them the memory address to set EIP as
    conn.send(b"Buffer size is 200 bytes. Overflow it and set EIP to 0x45454141\n(For this scenerio EIP can be overwritten directly following the overflow, 200-204 bytes, no offset needed):\n")
    print("Waiting for user to overflow buffer")
    #receive user response
    response = conn.recv(204)
    #check if response is correct length of 200 bytes plus the memory address
    if len(response) == 204:
        print("User overflowed buffer")
        if response[200:204] == b"EEAA":
            print("User set EIP correctly")
            conn.send(b"You set EIP correctly!\n")
            conn.send(b"SummitCTF{BabyBin_0verfl0wed_Buffer}\n")
            sleep(1)
            conn.close()
        else:
            print("User did not set EIP correctly")
            conn.send(b"You did not set EIP correctly\n")
            sleep(1)
            conn.close()
    else:
        print("User did not overflow buffer")
        conn.send(b"You did not overflow buffer\n")
        sleep(1)
        conn.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
with socket.socket() as s:
    #open port and wait for user to connect
    s.bind(("0.0.0.0", 1234))
    s.listen()
    print("Waiting for user to connect")
    while True:
        conn, addr = s.accept()
        threading.Thread(target=handler,args=(conn,), daemon=True).start() 

