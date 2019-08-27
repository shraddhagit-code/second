import socket
import sys
import logging

logging.basicConfig(filename="cfile.log",format='%(asctime)s %(message)s',filemode='w')

logger=logging.getLogger()

logger.setLevel(logging.DEBUG)

def ipvalidatn(ip):
        try:
            socket.inet_aton(ip)
            print('valid ip')
            #ip.split(".")
            a,b,c,d=ip.split(".")
            if 0<=int(a) and int(a)<=126:
                print('class A address')
            elif 128<=int(a) and int(a)<=191:
                print('class B')
            elif 192<=int(a) and int(a)<=223:
                print('class C')
            elif 224<=int(a) and int(a)<=239:
                print('class D')
            else:
                print('class E')
        except:
       # else:
            print('invalid ip')

try:
	f=open('config2.txt','r')
except:
        print('cant open file')
        logger.debug('cant open file')
        sys.exit()
ip=f.readline()
ipvalidatn(ip)
