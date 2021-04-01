import socket

HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MSG = "Disconnected"
ip = "192.168.1.233"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip,8080))
