FROM alpine
WORKDIR /src
COPY babyBin.py /src
RUN apk add --no-cache python3
EXPOSE 1234
CMD ["python3", "babyBin.py"]