import socket

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 56789))
    server_socket.listen(1)
    print('Server listening on port 56789...')

    while True:
        conn, addr = server_socket.accept()
        #ask if the client is npurja
        conn.sendall('Are you npurja? (y/n): '.encode())
        #get the response
        data = conn.recv(1024).decode().strip()
        #if the response is y, send the key
        if data == 'y':
            conn.sendall('\nClimb faster!\n'.encode())
            conn.sendall('\n\nNote to self: Keep eyes peeled for CVE-2022-22965 (Attackers seem to like: https://github.com/jayaram-yalla/CVE-2022-22965) \n'.encode())
            with open('/srv/ftp/npurja-backup-key', 'r') as f:
                conn.sendall(f.read().encode())
        else:
                conn.send('Nope, sorry!\n'.encode())
        conn.close()

if __name__ == '__main__':
    main()
