FROM node:lts-alpine

RUN npm install -g http-server

WORKDIR /app

COPY docking_sims_gui/package*.json ./

RUN npm install

COPY docking_sims_gui .

RUN npm run build

EXPOSE 8001

CMD [ "http-server", "dist" ]