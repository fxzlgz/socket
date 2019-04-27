import socket
#创建套接字对象
sockfd=socket.socket(socket.AF_INET,\
    socket.SOCK_STREAM)

#绑定地址
sockfd.bind(("0.0.0.0",8888))
#设置监听
sockfd.listen(3)
#等待客户端连
while True:
	print("waiting for connect.....")
	try:
		connfd,addr=sockfd.accept()
	except KeyboardInterrupt:
		print("server exit")
		break
	print("Connect from",addr)
	while True:
		data=connfd.recv(1024)
		if not data:
			break
		print("Receive message:",data.decode())

		n=connfd.send(b"Receive your message")
		print("Send %d bytes"%n)
	connfd.close()

sockfd.close()


























