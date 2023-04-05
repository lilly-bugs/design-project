import socket

def return_temp(hostname):

    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    mySocket.connect((hostname, 5560))

    msg = mySocket.recv(1024)
    temp = (msg.decode("utf-8"))

    temperature = str(temp)
    return temperature

#print(return_temp(hostname))
