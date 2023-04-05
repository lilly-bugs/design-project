import socket

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

hostname =  '192.168.0.101'

mySocket.connect((hostname, 10861))

msg = mySocket.recv(1024)
print(msg.decode("utf-8"))

