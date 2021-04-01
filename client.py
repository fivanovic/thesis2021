import time
import math
import socket

ip = "192.168.1.233" # Ip of raspberry pi

#connect to server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip, 8080))
print("CLIENT: CONNECTED")

#send a message
msg = "I AM CLIENT"
client.send(msg.encode())

#receieve and print
from_server = client.recv(4096).decode()
print("RECEIEVED :" + from_server)

#exit
client.close()
