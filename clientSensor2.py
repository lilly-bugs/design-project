import socket

def return_temp():

    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    hostname = '192.168.0.110'
    
    mySocket.connect((hostname, 5560))

    msg = mySocket.recv(1024)
    temp = (msg.decode("utf-8"))

    temperature = str(temp)
    return temperature

print(return_temp())
