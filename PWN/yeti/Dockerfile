FROM phusion/baseimage:focal-1.0.0-alpha1-amd64
RUN useradd -m challuser

# Set CWD to /app
WORKDIR /app

# Install packages
RUN apt-get update && apt-get install -y gcc xinetd curl patchelf

# Copy the current directory contents into the container at /app
ADD . /app
RUN sed -i -e 's/\r$//' ctf.xinetd
RUN mv ctf.xinetd /etc/xinetd.d/ctf

# Download pwninit from github
RUN curl https://github.com/io12/pwninit/releases/download/3.3.0/pwninit -o /bin/pwninit -L

# Set permissions
RUN chmod +x /bin/pwninit && chmod +x /app/compile.sh

# Compile the C program
RUN sed -i -e 's/\r$//' /app/compile.sh
RUN /bin/bash /app/compile.sh

# Make port 31337 available to the world outside this container
EXPOSE 31337

RUN echo "log_type = FILE /var/log/xinetd.log" >> /etc/xinetd.conf

# Run the executable when the container launches using xinetd
RUN sed -i -e 's/\r$//' /app/run.sh
RUN chmod +x /app/run.sh
CMD ["/app/run.sh"]