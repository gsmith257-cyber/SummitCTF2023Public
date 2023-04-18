#include <stdio.h>
#include <string.h>
#include "http.h"
#include "buf.h"
#include <sys/types.h>
#include <sys/socket.h>
#include <stdlib.h>
#include <stdbool.h>
#include <sys/sysinfo.h>
#include <unistd.h>

char* get_cpu_load()
{
    struct sysinfo info;
    if (sysinfo(&info) != 0)
    {
        return NULL;
    }
    double load = 1.0 - ((double)info.loads[0] / (double)(1 << SI_LOAD_SHIFT));
    char* load_str = (char*)malloc(32);
    if (load_str != NULL)
    {
        snprintf(load_str, 32, "%.2f", load);
    }
    return load_str;
}

char * execute_command(const char *command) {
    char *output = NULL;
    size_t output_length = 0;
    FILE *fp = popen(command, "r");
    if (fp == NULL) {
        perror("popen error");
        return NULL;
    }

    char buffer[128];
    while (fgets(buffer, sizeof(buffer), fp) != NULL) {
        size_t new_output_length = output_length + strlen(buffer);
        char *new_output = realloc(output, new_output_length + 1);
        if (new_output == NULL) {
            perror("realloc error");
            free(output);
            pclose(fp);
            return NULL;
        }
        output = new_output;
        strcpy(output + output_length, buffer);
        output_length = new_output_length;
    }

    if (pclose(fp) == -1) {
        perror("pclose error");
        free(output);
        return NULL;
    }

    return output;
}

static void send_http_response(int connfd, int status_code, int resp_size, char* content_type, char* response)
{
    char* status_text;
    switch (status_code)
    {
        case 200:
            status_text = "OK";
            break;
        case 400:
            status_text = "Bad Request";
            break;
        case 405:
            status_text = "Method Not Allowed";
            break;
        case 404:
            status_text = "Not Found";
            break;
        default:
            status_text = "Unknown";
            break;
    }

    char header[512];
    snprintf(header, 512, "HTTP/1.0 %d %s\r\nContent-Type: %s\r\nContent-Length: %d\r\n\r\n", 
             status_code, status_text, content_type, resp_size);

    write(connfd, header, strlen(header));
    write(connfd, response, resp_size);
    close(connfd);
}


void handle_debug(int connfd, char* path)
{
    /* For uname */
    /* get debug parameters */
    char * command = malloc(256);
    strcpy(command, &path[11]);

	if (strncmp(command, "ping", 4) == 0)
	{
		char *out = "{\"message\": \"pong\"}";
		send_http_response(connfd, 200, strlen(out), "application/json", out);
		free(command);
		return;
	} else if (strncmp(command, "stats", 5) == 0)
	{
		char * debug_out = malloc(32768);
		int count = snprintf(debug_out, 12, "{\"path\": \"}") - 1;
		count += sprintf(&debug_out[count], path);
		count += snprintf(&debug_out[count], 3, "\",");
		count += sprintf(&debug_out[count], "\"load\": \"%s\"}", get_cpu_load());
		send_http_response(connfd, 200, count, "application/json", debug_out);
		free(command);
		free(debug_out);
		return;
	} else if (strncmp(command, "uname", 5) == 0)
	{
		char * uname_out = malloc(128);
		char * cmd_out = execute_command("uname -a");
		char * json_out = malloc(512);
		int count = sprintf(json_out, "{\"message\": \"%s\"}", cmd_out);
		free(cmd_out);
		send_http_response(connfd, 200, count, "application/json", json_out);
		free(json_out);
		return;
	}

	char *out = "{\"error\": \"unsupported operation\"}";

	send_http_response(connfd, 400, strlen(out), "application/json", out);
	free(command);
}


static int read_file(struct http_message * msg, char * buffer)
{
    long length;
    char webroot_path[256] = "webroot";
    memcpy(&webroot_path[7], msg->path, msg->path_len);

    FILE* f = fopen(webroot_path, "rb");
    if (f)
    {
        fseek(f, 0, SEEK_END);
        length = ftell(f);
        fseek(f, 0, SEEK_SET);
        if (buffer)
        {
            fread(buffer, 1, length, f);
            fclose(f);
            return length;
        }
        fclose(f);
    }
    return -1;
}


void parse_http_message(struct http_message * ptr, int connfd)
{
	/* The first read will give us the HTTP info and PATH */
	int read_size = read_to_crlf();
	int first_line_size = read_size;
	int last_ptr_loc = read_size;
	char * foo = malloc(read_size + 1);
	memcpy(foo, loc_to_ptr(0), read_size);
	foo[read_size] = 0;

	/* TODO: Headers unimplemented */
	while(read_size != 2)
	{
		/* Do next read */
		int mem_loc = read_to_crlf();
		read_size = mem_loc - last_ptr_loc;
		last_ptr_loc = mem_loc;
	}

	/* Done reading all lines of the HTTP Message */
	/* Sooo let's see if it's GET first */
	if (strncmp("GET", foo, 3) != 0)
	{
		printf("Oh no! Not a GET method :(\n");
		ptr->method = UNKNOWN;
		/* Check method in the caller */
		return;
	} else {
		ptr->method = GET;
	}

	/* The path component starts at offset 4 of this new string and ends at the space */
	int i = 4;
	for (i = 4; i < first_line_size; i++)
	{
		if (foo[i] == ' ')
		{
			break;
		}

		foo[i - 4] = foo[i];
	}

	foo[i - 4] = 0;

	ptr->path = foo;
	ptr->path_len = i;
}

void * handle_http_message(void * ptr)
{
	int connfd = (long long) ptr;
	
	/* initialize buffering */
	init_fd(connfd);

	/* create struct on stack */
	struct http_message msg;
	memset(&msg, 0, sizeof(struct http_message));
	parse_http_message(&msg, connfd);

	if (msg.method == UNKNOWN)
	{
		char *out = "<h1>method not implemented :(</h1>";
		send_http_response(connfd, 405, strlen(out), "text/html", out);
		return NULL;
	}

	/* Check if they are doing the bad thing >:( */
	if (strstr(msg.path, ".."))
	{
		char *out = "<h1>stahp</h1>";
		send_http_response(connfd, 400, strlen(out), "text/html", out);
		return NULL;
	}

	/* handle api call */
	if (strncmp("/api/debug/", msg.path, 11) == 0)
	{
		handle_debug(connfd, msg.path);
		return NULL;
	}

	char *file = msg.path;

	/* See if the path is just / */
	if (strcmp(file, "/") == 0)
	{
		msg.path = "/index.html";
		msg.path_len = 12;
	}

	/* this should be big enough for our purposes, the files we serve should not exceed this in theory! */
	char * file_buffer = malloc(65536);
	int file_length = read_file(&msg, file_buffer);

	if (file_length < 0)
	{
		char *out = "<h1>not found</h1>";
		send_http_response(connfd, 404, strlen(out), "text/html", out);
		return NULL;
	}

	char * mime_type = "text/html";


	/* i know that strstr looks everywhere in the string but im too lazy to implement endswith */
	if (strstr(file, ".gif")) {
		mime_type = "image/gif";
	}

	send_http_response(connfd, 200, file_length, mime_type, file_buffer);
	return NULL;
}
