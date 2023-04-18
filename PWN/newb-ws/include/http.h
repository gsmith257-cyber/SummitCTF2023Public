enum method_type
{
	GET,
	UNKNOWN
};

struct header
{
	char * key;
	char * value;
};

struct http_message
{
	enum method_type method;
	char * path;
	size_t path_len;
	
	/* I'l take care of this later */
	char ** headers;
};

void parse_http_message(struct http_message *, int);
void * handle_http_message(void *);
