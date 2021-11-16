FROM node:14-alpine AS development
ENV NODE_ENV development

WORKDIR /reports_ui

COPY ./reports_ui/package.json .
COPY ./reports_ui/package-lock.json .
RUN npm install

COPY ./reports_ui .

EXPOSE 3000

CMD [ "npm", "start" ]