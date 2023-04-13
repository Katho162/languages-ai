FROM node:19-alpine

WORKDIR /usr/src/app

COPY packages*.json ./

ADD package.json /usr/src/app/package.json

RUN npm install

RUN npm install react-scripts -g

COPY

EXPOSE 3000

CMD ["npm", "start"]