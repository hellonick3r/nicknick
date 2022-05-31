#client
import  os
import socket
os.system('clear')
host = 'localhost'
port = 1102
name = input('name: ')
s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
s.connect((host, port))
print('connected')
while True:
	text = input('text: ')
	s.send(text.encode('utf-8'))
	msg = s.recv(1024).decode('utf-8')
	print(msg)