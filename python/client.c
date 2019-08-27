#include"headers.h"

int fd,ret;
char buff[100];
struct sockaddr_in saddr;
int slen = sizeof(saddr);

int main(int argc, char **argv){

	if(argc<3){
		puts("input: ClientEXE wkpno_serv servIP");
		return 0;
	}

	puts("Creating Client socket...");
	fd = socket(AF_INET,SOCK_STREAM,0);

	if(fd<0){
		perror("Socket");
		return 0;
	}

	puts("Client Socket created");
	puts("Connecting...");

	saddr.sin_family = AF_INET;
	saddr.sin_port = htons(atoi(argv[1]));
	saddr.sin_addr.s_addr = inet_addr(argv[2]);

	if(connect(fd,(struct sockaddr *)&saddr,slen)<0){
		perror("Connect");
		close(fd);
		return 0;
	}
	puts("Connected");

	while(1){

		puts("Enter msg/req for server");
		gets(buff);
		puts("Sending...");

		if(send(fd,buff,100,0)<0){
			perror("Send");
			break;
		}
		puts("sent");
		memset(buff,0,100);

		puts("Waiting for echo reply...");
		ret = recv(fd,buff,100,0);

		if(ret<0){
			perror("recv");
			break;
		}
		else if(ret == 0){
			puts("Server abnormally terminated");
			break;
		}
		else{
			printf("REcvd : %s \n",buff);
	
			if(strcmp(buff,"quit")==0){
				puts("Server formally terminating connection");
				break;
			}
		}
	}

	puts("Closing connection with server");
	close(fd);
	puts("Client Terminated");

	return 0;
}
