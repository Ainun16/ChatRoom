import time
import socket
import sys
from _thread import *

new_socket = socket.socket()
host_name = socket.gethostname()
s_ip = '192.168.199.4'

port = 8080
ThreadCount = 0

new_socket.bind(('192.168.199.4', port))
print ("Binding successful!")
print ("This is your IP: ", s_ip)

name = input('Enter name:')

print ('Waiting for client')
new_socket.listen(5)

conn, add = new_socket.accept()

print ("Receive connection from ", add[0])
print ('Connection Established. Connected from: ' , add[0])

client = (conn.recv(1024)).decode()
print(client + ' has connected.')
print('-------------------------------')
print('Welcome to the Hey Chat Room!!!')
print('-------------------------------')

conn.send(name.encode())

while True:
        message = input('Me:')
        conn.send(message.encode())
        message = conn.recv(1024)
        message = message.decode()
        print(client, ':', message)
        
while True:
        Client, address = new_socket.accept()
        print ('Connected to: ' + address[0] + ':' + str(address[1]))
        start_new_thread (threaded_client, (Client))
        ThredCount +=1
        print ('Thred Number: ' + str(ThresCount))

new_socket.close()

