import socket

print("enter ip:")
ip=input()
print("enter port No. :")
portno=input()

cli=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

cli.connect((ip,int(portno)))
full_msg = ''
msg = input("Enter msg/request to send : ")

while msg != 'quit':
    snd = msg.encode()
    cli.send(snd)
    from_server=cli.recv(1000)
    print(from_server.decode("utf-8"))
    #if len(from_server) <= 0:
     #   break
    full_msg +=from_server.decode("utf-8")
    msg = input("Enter msg/ request to send : ")


print(full_msg)
cli.close()

print(from_server)
