import sys
import logging


logging.basicConfig(filename="afile.log",format='%(asctime)s %(message)s',filemode='w')
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)

def fibb(n):
	a=0
	b=1
	esum=b
	if n<0:
		print('pass valid input')
		logger.debug('pass valid input')
		'''print(a)
		for i in range(2,n):
			c=a-b
			a=b
			b=c
			print(c)'''
	elif n==1:
		print(a)
	else:
		print(a)
		print(b)
		for i in range(2,n):
			c=a+b
			a=b
			b=c
			print(c)
			if i%2:
				esum+=c
	print('even position no sum=',esum)
try:
	f=open('config','r')	
except: 
	print('cant open file\n')
	logger.debug('cant open file\n')
	sys.exit()
try:
	no=int(f.readline())
except:
	print('invalid input\n')
	logger.debug('invalid input\n')
	sys.exit()
fibb(no)

