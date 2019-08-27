import socket
print("enter ip :")
ip=input()
print("enter port no :")
portno=input()

ser = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("socket created\n")

ser.bind((ip, int(portno)))
print("bound\n")

ser.listen(5)

from_client=''
print("waiting for connection\n")
while True:
    conn, addr=ser.accept()
    print("connection from address has been establish!\n")
    conn.send(bytes("welcome to server!\n","utf-8"))
    conn.send(bytes("hii, I am server!!!\n","utf-8"))
    while True:
        data = conn.recv(4096)
        if not data: break
        # from_client +=data
        print("data received is -", data)
        conn.send(bytes(str(data),"utf-8"))

conn.close()
    
print('client disconnect\n')

