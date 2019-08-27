import socket
import logging
import os
#creating n configriing logger
logging.basicConfig(filename="logtestout.log",
                    format='%(asctime)s %(message)s',filemode='w')

logger=logging.getLogger()

logger.setLevel(logging.DEBUG)

#def child():
 #   print("new connect

#reading from file 
f=open('configc.txt','r')
ip=f.readline()
portno=f.readline()

ser = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("socket created\n")

ser.bind((ip, int(portno)))
print("bound\n")

ser.listen(5)

from_client=''
print("waiting for connection\n")
while True:
    conn, addr=ser.accept()
    print("connection has been establish! and address is :\n",addr)
    if os.fork()==0: 
        while True: 
            print('waiting for clients msg...')
            data = conn.recv(4096)
            msg=data.decode() 
            print("from client data received -",msg)
            if msg=='quit':
                break
            print('enter data to send')
            send_dat=input()    
            while len(send_dat)==0:
                print('next time please enter some text')
                send_dat=input()    
            conn.send(send_dat.encode())
        os._exit(0)    
print('client disconnected\n')
conn.close()
