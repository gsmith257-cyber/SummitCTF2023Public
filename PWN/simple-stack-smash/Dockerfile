FROM phusion/baseimage:focal-1.0.0-alpha1-amd64
RUN useradd -m challuser
WORKDIR /src
RUN dpkg --add-architecture i386
RUN apt-get update
RUN apt-get install -y xinetd g++ make sl-modem-daemon:i386 gcc-multilib

# Copy needed files
COPY ctf.xinetd /etc/xinetd.d/ctf
COPY Makefile /src
COPY flag.txt /src
COPY smash.c /src
COPY run.sh /src

# Compile 
RUN make

# Set permissions for files
RUN chmod 744 /src/flag.txt
RUN chmod +x /src/run.sh
RUN sed -i -e 's/\r$//' /src/run.sh
RUN sed -i -e 's/\r$//' /etc/xinetd.d/ctf
# Run and expose
CMD ["/bin/bash", "/src/run.sh"]
EXPOSE 1337
