FROM phusion/baseimage:focal-1.0.0-alpha1-amd64
RUN useradd -m challuser
WORKDIR /src
RUN apt-get update
RUN apt-get install -y xinetd g++ make

# Copy needed files
COPY ctf.xinetd /etc/xinetd.d/ctf
COPY Makefile /src
COPY flag.txt /src
COPY main.cpp /src
COPY run.sh /src

# Compile 
RUN make

# Set permissions for files
RUN chmod 744 /src/flag.txt
RUN chmod +x /src/run.sh

# Run and expose
CMD ["/src/run.sh"]
EXPOSE 1337