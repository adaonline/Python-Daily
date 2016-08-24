#coding=UTF-8
import socket
HOST='localhost'
PORT=25678
BUFSIZE=1024
ADDR=(HOST,PORT)

tcpCliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpCliSock.connect(ADDR) #把套接字连接到指定服务器的地址上
while True:
	data=raw_input('>')
	if not data:
		break
	tcpCliSock.send(data)#发送
	data=tcpCliSock.recv(BUFSIZE)#接受
	if not data:
		break
	print data
tcpCliSock.close()
	