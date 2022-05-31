import os
import socket
os.system('clear')
#setting ip port 
ip = 'localhost'
port =1102

#สร้าง socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ip, port))
s.listen()
while True:
	print('waiting for connect')
	#เชื่อมต่อกับ client
	connection, client_ads  = s.accept()
	try:
		while True:
			data = connection.recv(1024).decode('utf-8')
			if data == 'hi':
				connection.send(('hi user \033[32m'+ str(client_ads[1])+'\033[0m').encode('utf-8'))
			else:
				print(data)
	finally:
			connection.close()
			print("closed connection")