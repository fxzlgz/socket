#http server 1.0
from socket import*
#处理客户端请求
def handle_request(c):
    print("Request from:",c.getpeername())
    request=c.recv(4096).decode()
    print(request)
    #获取请求行
    request_line=request.splitlines()
    for item in request_line:
        print(item)

    try:
        f=open('index.html')
    except IOError:
        response="HTTP/1.1 404 Not Found\r\n"
        response+='\r\n'
        response+='==sorry not found=='
    else:
        response="HTTP/1.1 200  OK\r\n"
        response+='\r\n'
        response+=f.read()

    finally:
        c.send(response.encode())
        f.close()

#创建套接字函数
def main():
    s=socket()
    s.setsockopt(SOL_SOCKET,\
    SO_REUSEADDR,1
    )
    s.bind(('0.0.0.0',8000))
    s.listen(3)
    print("Listen the port 8000....")
    while True:
        c,addr=s.accept()
        handle_request(c)
        c.close()


if __name__=="__main__":
    main()
