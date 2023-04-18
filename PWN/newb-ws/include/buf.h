#define INITIAL_BUF_SIZE 1024

char * loc_to_ptr(int);
static void buf_sock_read();
int read_to_crlf(void);
void init_fd(int);
