import socket


class Network:

    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = '192.168.0.103'
        self.port = 8080
        self.addr = (self.server, self.port)
        self.pos = self.connect()

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(str(e))

    def getPos(self):
        return self.pos

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(str(e))


n = Network()
print(n.send('Hello!'))
print(n.send('Working!'))

