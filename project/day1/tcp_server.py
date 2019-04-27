"""
socket编程
套接字：实现网络编程进行数据传输的一种技术手段
"""
"""
import socket
"""
"""
sock_stream
以字节流方式进行数据传输，实现tcp网络传输方案---面向连接--tcp
"""
"""
sock_dgram
以数据报形式传输数据，实现udp网络传输方案---面向无连接--udp
"""

"""
severe 

"""
"""
tcp_server.py
"""
import socket
#创建套接字对象
sockfd=socket.socket(socket.AF_INET,\
    socket.SOCK_STREAM)

#绑定地址
sockfd.bind(("0.0.0.0",9999))
#设置监听
sockfd.listen(3)
#等待客户端连接
print("waiting for connect.....")
connfd,addr=sockfd.accept()
print("Connect from",addr)

#消息收发
data=connfd.recv(1024)
print("Receive message:",data.decode())

n=connfd.send(b"Receive your message")
print("Send %d bytes"%n)
connfd.close()
sockfd.close()


























