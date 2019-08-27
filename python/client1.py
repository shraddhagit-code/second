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

cli=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("socket created\n")

cli.connect((ip,int(portno)))

msg=''
while msg != 'quit':
    msg = input("Enter msg/request to send : ") 
    while len(msg)==0:
        print('next time please enter some text')
        msg = input("Enter msg/request to send : ") 
    cli.send(msg.encode())
    from_server=cli.recv(1024)
    recv = from_server.decode()
    print('Server replied as : ',recv)

print('client exited\n')
cli.close()
