import time
import socket
import sys

socket_server = socket.socket()
server_host = '192.168.199.4'
ip = '192.168.199.3'
port = 8080

print ('This is your IP address:' , ip)

server_host = input('Enter friend\'s IP address:')
name = input('Enter name:')

print ('Waiting for connection')
socket_server.connect(('192.168.199.4', port))

socket_server.send(name.encode())
server_name = socket_server.recv(1024)
server_name = server_name.decode()

print (server_name, 'has joined....')
print ('-------------------------------')
print ('Welcome to the Hey Chat Room!!!')
print ('-------------------------------')

while True:
        message = (socket_server.recv(1024)).decode()
        print(server_name, ":", message)
        message = input ("Me:")
        socket_server.send(message.encode())

