#include <stdlib.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <stdio.h>
#include "buf.h"

static __thread char *p = NULL;
static __thread int buf_size = 0;
static __thread int recv_ptr = 0;
static __thread int read_ptr = 0;
static __thread int fd = -1;

void init_fd(int f)
{
	fd = f;
}

char * loc_to_ptr(int loc)
{
	return p + loc;
}

/* read to the CRLF inclusive */
int read_to_crlf(void)
{
	/* Do multiple reads until we get to the CRLF */
	while (1)
	{
		if (recv_ptr == buf_size)
			buf_sock_read();
		
		for (int i = read_ptr; i < recv_ptr - 1; i++)
		{
			if (p[i] == '\r' && p[i + 1] == '\n')
			{
				read_ptr = i + 2;
				return i + 2;
			}	
		}	
	}

}

static void buf_sock_read()
{
	if (fd < 0)
	{
		return;
	}

	if (p == NULL)
	{
		buf_size = INITIAL_BUF_SIZE;
		p = malloc(buf_size);
	}

	/* Reallocate buffer, we got some more data coming in */
	if (recv_ptr == buf_size)
	{
		buf_size *= 2;
		p = realloc(p, buf_size);
	}

	ssize_t read_size = recv(fd, p + recv_ptr, buf_size - recv_ptr, 0);

	recv_ptr += read_size;	
}
