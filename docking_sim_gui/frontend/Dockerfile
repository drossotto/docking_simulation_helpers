FROM node:18 AS frontend-builder

WORKDIR /app/frontend

COPY ./package*.json ./

RUN npm install

COPY . ./

RUN npm run build


FROM nginx:alpine

WORKDIR /usr/share/nginx/html

RUN rm -rf ./*

COPY --from=frontend-builder /app/frontend/dist .

EXPOSE 80

ENTRYPOINT [ "nginx", "-g", "daemon off;" ]