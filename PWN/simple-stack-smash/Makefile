main: smash.c
	$(CC) smash.c -fno-stack-protector -no-pie -o simple-stack-smash -m32 -mpreferred-stack-boundary=2

clean:
	rm -f simple-stack-smash
