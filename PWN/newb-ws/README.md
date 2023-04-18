# Building & Running on M1 MBP

```
docker buildx build -t newbws --platform linux/amd64 .
```

```
docker run -p 80:80 --platform linux/amd64 -t newbws
```