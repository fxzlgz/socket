from socketserver import *

# class Server(ForkingTCPServer):
#     pass
class Server(ForkingMixIn,TCPServer):
    pass

class Handler(StreamRequestHandler):
    def handle(self):
        # print("Connect from",\
        #     self.request.getpeername())
        print("Connect from",\
            self.cilent_address)
        while True:
            data=self.request.recv(1024).decode()
            if  not data:
                break
            print(data)
            self.request.send(b"ok")

server=Server(('0.0.0.0',8888),Handler)
server.serve_forever()
