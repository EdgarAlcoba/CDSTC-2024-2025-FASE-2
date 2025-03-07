FROM node:alpine

WORKDIR /app

COPY package*.json .

RUN npm install

COPY . .

ENV REACT_APP_TESTNAME=testName

EXPOSE 3030

CMD ["npm", "start"]