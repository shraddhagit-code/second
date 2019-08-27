import socket
import sys

global ser
def main():
    f=open('config.txt','r')
    ip=f.readline()
    portno=f.readline()
    ser = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    q=f.readline()
    print("socket created\n")
    ser.bind((ip,int(portno)))
    print("bound\n")
    ser.listen(int(q))
    conn()


def conn():
    from_client=''
    print("waiting for connection\n")
    conn, addr=ser.accept()
    print("connection has been establish! and address is :\n",addr)
    while True: 
        print('waiting for clients msg...')
        data = conn.recv(4096)
        msg=data.decode() 
        print("from client data received -",msg)
        if msg=='quit':
            break
        print('enter data to send')
        send_dat=input()    
        conn.send(send_dat.encode())
    print('client disconnected\n')
    conn.close()
'''
def main():
    f=open('config.txt','r')
    ip=f.readline()
    portno=f.readline()
    ser = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    q=f.readline()
    print("socket created\n")
    ser.bind((ip,int(portno)))
    print("bound\n")
    ser.listen(int(q))
    conn()
'''
main()
