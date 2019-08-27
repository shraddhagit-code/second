import sys
import logging


logging.basicConfig(filename="bfile.log",format='%(asctime)s %(message)s',filemode='w')
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)

def mul3n5(n):
	total=0
	for i in range(1,n):
		if i%3==0 and i%5==0:
			print('multiple of 3 & 5: ',i)
			total+=i
	if total>0:
		print('sum of no which are multiple of 3 & 5 is :',total)
	else:
		print('no multiple of 3 and 5 found')


try:
	f=open('configb','r')	
except: 
	print('cant open file\n')
	logger.debug('cant open file\n')
	sys.exit()
try:
	no=int(f.readline())
except:
	print('invalid input')
	logger.debug('invalid input\n')
	sys.exit()
mul3n5(no)

