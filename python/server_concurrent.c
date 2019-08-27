#include"headers.h"

int sfd,cfd;
struct sockaddr_in saddr,caddr;
int slen=sizeof(saddr),clen=sizeof(caddr);
int ret;char buf[100];

void clientInfo(int cfd,struct sockaddr_in caddr)
{
	char *clientIP=inet_ntoa(caddr.sin_addr);
	unsigned short int portNo=ntohs(caddr.sin_port);
	puts("Client Info...");
	printf("Client's IP : %s\nClient's port No : %d\n",clientIP,portNo);
	printf("Client File Descriptor : %d\n",cfd);

	return;
}

void signalHandler(int status)
{
	wait(&status);
	printf("\nClient Process : %d Exitted\n",getpid());
}

int main(int argc,char **argv)
{
	signal(SIGCHLD,signalHandler);
	if(argc<2)
	{
		puts("input : serverExe wkpNo\n");
		return 0;
	}
	puts("Creating Server Socket...");

	sfd=socket(AF_INET,SOCK_STREAM,0);
	if(sfd<0)
	{
		perror("socket");
		return 0;
	}
	puts("Server Socket Created");
	puts("Binding...");

	saddr.sin_family=AF_INET;
	saddr.sin_port=htons(atoi(argv[1]));
	saddr.sin_addr.s_addr=inet_addr("0.0.0.0");
	if(bind(sfd,(const struct sockaddr*)&saddr,slen)<0)
	{
		perror("bind");
		close(sfd);
		return 0;
	}
	puts("Binding Done");

	puts("Creating Connection queue of size 1");
	if(listen(sfd,1)<0)
	{
		perror("listen");
		close(sfd);
		return 0;
	}
	puts("Queue Created");
	while(1)
	{
		l1:
		puts("Waiting to accept connection request from client...");
		cfd=accept(sfd,(struct sockaddr*)&caddr,&clen);
		if(cfd<0)
		{
			perror("accept");
			goto l1;
		}
		puts("Connection from Client Accepted");
		clientInfo(sfd,caddr);
		if(fork()==0)
		{
			while(1)
			{
				puts("Waiting for msg/req from Client...");
				ret=recv(cfd,buf,100,0);

				if(ret<0)
				{
					perror("recv");
					break;
				}
				else if(ret==0)
				{
					puts("Client Abnormally terminated");
					break;
				}
				else
				{
					printf("Recvd : %s\n",buf);
					puts("Echoing back...");
					if(send(cfd,buf,100,0)<0)
					{
						perror("send");
						break;
					}
					puts("Echoed...");
					if(strcmp(buf,"quit")==0)
					{
						puts("Client Formally Terminating Connection...");
						break;
					}
				}
			}
			puts("Closing Connection with Client");
			clientInfo(cfd,caddr);
			close(cfd);
			exit(0);
		}

	}
	puts("Server Going Down");
	close(sfd);
	return 0;
}

