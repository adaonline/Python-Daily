#coding=UTF-8
import socket
from time import ctime

HOST=''#HOST 变量为空，表示 bind()函数可以绑定在所有有效的地址上
PORT=25678
BUFSIZE=1024
ADDR=(HOST,PORT)

tcpSerSock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#生成套接字
tcpSerSock.bind(ADDR)#把套接字绑定到服务器的地址上
tcpSerSock.listen(5) #一次性接受多少连接

while True:
	print u'等待连接...'
	tcpCliSock,addr=tcpSerSock.accept()#阻塞等待连接的到来
	print u'...连接来自:',addr
	
	while True:
		data=tcpCliSock.recv(BUFSIZE)
		if not data:
			break #为空则说明客户断开
		tcpCliSock.send('[%s] %s'%(ctime(),data))

tcpCliSock.close()
tcpCliSock.close()	

