FROM phusion/baseimage:focal-1.0.0-alpha1-amd64
RUN useradd -m challuser
WORKDIR /src
RUN apt-get update
RUN apt-get install -y python3 python3-pip
RUN pip3 install virtualenv

# Copy needed files
COPY app.py /src/
COPY flag.txt /src/
COPY run.sh /src/
COPY ./static/ /src/static/
COPY ./templates/ /src/templates/
COPY requirements.txt /src/

RUN virtualenv -p python3 venv
RUN chmod +x ./venv/bin/activate
RUN ./venv/bin/activate && pip install -r requirements.txt

# Set permissions for files
RUN chmod 744 /src/flag.txt
RUN chmod +x /src/run.sh

# Run and expose
CMD ["/src/run.sh"]
EXPOSE 5000