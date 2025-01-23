FROM alpine:latest

RUN apk update && \
    apk add --no-cache sudo nano bash curl wget

WORKDIR /usr

COPY . .

RUN chmod +rwx test_server.sh

EXPOSE 8000



