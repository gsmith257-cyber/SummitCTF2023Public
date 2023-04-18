FROM python:3-alpine

# Create app directory
WORKDIR /site

# Install app dependencies
COPY requirements.txt ./

RUN pip install -r requirements.txt

RUN export FLASK_APP=OneTextPlease

# Bundle app source
COPY . .

RUN mv flag.txt /flag.txt
RUN chmod 444 /flag.txt

EXPOSE 5000
CMD [ "python", "challenge/run.py"]