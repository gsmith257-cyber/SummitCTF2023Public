FROM alpine:3.15
WORKDIR /src

# Install python
ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python

#Copy files to /src
COPY mithrandir.py /src/

CMD python3 /src/mithrandir.py
EXPOSE 2941
