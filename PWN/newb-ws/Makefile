CC=/usr/local/musl/bin/musl-gcc
CFLAGS=-static -Iinclude -fPIE -fPIC
# Musl libc is statically compiled with -fPIE and -fPIC
LDFLAGS=-s -Wl,-Bstatic -L/usr/local/musl/lib -lc -Wl,-Bdynamic -lpthread -pie -fPIE -fPIC
OBJ=build/main.o build/http.o build/buf.o
TARGET=build/httpd

build/%.o: src/%.c
	$(CC) -c -o $@ $< $(CFLAGS)

$(TARGET): $(OBJ)
	$(CC) -o $@ $^ $(LDFLAGS)
clean:
	rm -rf build
