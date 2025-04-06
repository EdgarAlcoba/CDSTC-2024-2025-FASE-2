FROM node:alpine

WORKDIR /app

COPY package*.json .

RUN npm install

COPY . .

ENV REACT_APP_TESTNAME=testName

RUN apk add --no-cache nginx bash

EXPOSE 80
EXPOSE 443

COPY nginx.conf /etc/nginx/nginx.conf
COPY default.conf /etc/nginx/conf.d/default.conf
COPY ssl /etc/ssl/

RUN npm run build

CMD ["sh", "-c", "nginx -g 'daemon off;'"]