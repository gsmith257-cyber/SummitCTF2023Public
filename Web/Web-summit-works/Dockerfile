FROM ubuntu
WORKDIR /src
#update the repository sources list
ARG DEBIAN_FRONTEND=noninteractive
RUN apt update

# Installing dependencies
RUN apt-get install -y python3 python3-pip
RUN apt-get install -y mariadb-server
RUN apt-get install -y libmariadb3 libmariadb-dev
RUN apt-get install -y firefox
RUN apt-get install -y xvfb
RUN apt-get install -y supervisor

# Setting up python virtualenv
RUN pip3 install virtualenv

#Copying necessary files
COPY app.py /src/
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY client.py /src/
COPY geckodriver /src/
COPY requirements.txt /src/
COPY ./static/ /src/static/
COPY ./templates/ /src/templates/
COPY server.sh /src/
COPY client.sh /src/

# Making necessary files executable
RUN virtualenv -p python3 venv
RUN chmod +x ./venv/bin/activate
RUN chmod +x /src/server.sh
RUN chmod +x /src/client.sh
RUN ./venv/bin/activate && pip3 install -r requirements.txt


CMD ["/usr/bin/supervisord"]
EXPOSE 5000

