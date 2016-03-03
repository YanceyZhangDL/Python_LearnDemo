#! /usr/bin/env python
# -*- coding: utf-8 -*-

#Wrote a web brower
#made a connection
#sent a request down
#got the data back
#showed it to ourselves on the screen

#HTTP Protocol Request in Python
import socket
mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#首先，程序与服务器www.py4inf.com在80端口建立一个连接，作为网络浏览器
mysock.connect(('www.py4inf.com',80))#(Host,Port)Establish a connection 
#Http协议要求，必须发送GET命令，并在后面跟一个空白行（telnet和GET的结合）
mysock.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')##必须两个回车才能发送请求，因为其中一个是空白行
#发送空白行之后,我们编写一个循环,从套接字中接收512个字符的数据片段,并打印出这些数据,直到没有数据可以读入,即recv()返回一个空字符串。
while True:
	data = mysock.recv(512)#接收数据，receive the socket
	if(len(data) < 1):
		break
	print data#我们获取到的数据
mysock.close()#关闭

