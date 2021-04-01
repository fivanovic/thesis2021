import socket
import time
import threading

ip = socket.gethostbyname(socket.gethostname())
#start server
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind((ip, 8080))
serv.listen(5)
print("SERVER: started")

while True:
    conn, addr = serv.accept()
    from_client = ''
    print("SERVER: connection to client established")

    while True:
        #receieve data and print
        data = conn.recv(4096).decode()
        if not data: break
        from_client += data
        print("Received: " + from_client)

        #send message back to client
        msg = "I AM SERVER"
        conn.send(msg.encode())
        time.sleep(0.5)

    #close connection and exit
    conn.close()
    break
