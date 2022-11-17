#!/usr/bin/python3
import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#host = '150.250.133.235'
host = socket.gethostname()

port = 555

clientsocket.connect(('150.250.133.235', port))

# maximum amount of data allowed to come through the port
message = clientsocket.recv(1024)

clientsocket.close()

print(message.decode('ascii'))
