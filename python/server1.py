import socket
import logging
#logfile

logging.basicConfig(filename="logtestout.log",
                   format='%(asctime)s %(message)s',filemode='w')

logger=logging.getLogger()
logger.setLevel(logging.DEBUG)

#reading from file containing ip and port no
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
    while len(send_dat)==0:
        print('next time please enter some text')
        send_dat=input()    
    conn.send(send_dat.encode())

print('client disconnected\n')
conn.close()
