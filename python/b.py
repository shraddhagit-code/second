#import 
f=open('data','r')
print("enter number: ")
#no=input()
no=f.readline()
addn=0
for x in range(int(no)):
    if x%3==0:
        if x%5==0:
            print(x)
            addn+=x
print('sum=',addn)
