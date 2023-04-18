#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netinet/ip.h>
#include <arpa/inet.h>
#include <string.h>
#include <pthread.h>
#include "http.h"

/* Code stolen from: https://gist.github.com/browny/5211329 */
bool server_loop(unsigned short port)
{
	int listenfd = 0, connfd = 0;
	struct sockaddr_in serv_addr;

	listenfd = socket(AF_INET, SOCK_STREAM, 0);
	
	if (listenfd < 0)
	{
		printf("Oh no! Couldn't create server socket\n");
		return false;
	}

	int opt = 1;
	
	if (setsockopt(listenfd, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt))) {
        perror("setsockopt");
        exit(EXIT_FAILURE);
    }

	memset(&serv_addr, 0, sizeof(serv_addr));

	serv_addr.sin_family = AF_INET;
	serv_addr.sin_addr.s_addr = htonl(INADDR_ANY);
	serv_addr.sin_port = htons(port);

	int bind_ret = bind(listenfd, (struct sockaddr*)&serv_addr, sizeof(serv_addr));
	if (bind_ret < 0)
	{
		printf("Oh no! Couldn't bind port %d\n", port);
		return false;
	}
	
	int listen_ret = listen(listenfd, 10);
	if (listen_ret < 0)
	{
		printf("Oh no! Couldn't listen on port %d :(\n", port);
		return false;
	}

	/* Welisten for connections forever. */
	printf("Yay! We are listening on port %d!\n", port);
	while(1)
	{
		connfd = accept(listenfd, (struct sockaddr*)NULL, NULL);
		printf("Got a connection! :D :D :D, spawning new server thread...\n");

		pthread_t my_thread;	
		pthread_create(&my_thread, NULL, handle_http_message, (void *) (long long) connfd);
	}
	return true;
}

int main(int argc, char ** argv)
{
	printf("Welcome to my first C web server! I did this because I don't like the bloat of other modern web servers.\n");
	if (argc < 2)
	{
		printf("Specify a port, dummy!\n");
		return 1;
	}

	unsigned short port = atoi(argv[1]);
	if (port == 0)
	{
		printf("Who do you think you are? Give me a correct port.\n");
		return 1;
	}

	if(!server_loop(port))
	{
		printf("Something went wrong... Oh no :(\n");
		return 1;
	}
	return 0;
}
