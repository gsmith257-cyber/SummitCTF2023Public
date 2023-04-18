FROM phusion/baseimage:focal-1.0.0-alpha1-amd64
WORKDIR /src

#Installing python and xinetd
RUN apt-get update -y
RUN apt-get install -y python3 xinetd

#Creating low-priv user
RUN useradd -m flagman
WORKDIR /src

#Copy files to /src
COPY ctf.xinetd /etc/xinetd.d/ctf
COPY burgerland.py /src
COPY flag.txt /src 
COPY run.sh /src
COPY exec.sh /src
RUN chmod +x run.sh
RUN chmod +x exec.sh
RUN chmod +x burgerland.py
CMD ["/src/run.sh"]
