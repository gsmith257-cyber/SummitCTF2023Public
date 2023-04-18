FROM node:latest

RUN mkdir app/
WORKDIR /app
COPY Site/ .
RUN npm install
RUN npm run build
EXPOSE 3000
CMD ["npm", "run", "start"]