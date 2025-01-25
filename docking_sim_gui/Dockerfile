#Build for the frontend#
FROM node:18 AS frontend-builder

WORKDIR /app/frontend

COPY frontend/package*.json ./

RUN npm install

COPY frontend/ ./

RUN npm run build


#Build for the backend#
FROM python:3.9-bullseye AS backend-builder

WORKDIR /app

COPY backend/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY backend ./backend

COPY --from=frontend-builder /app/frontend/dist ./frontend/dist

WORKDIR /app/backend


#Build the NGINX proxy server#

FROM nginx:stable AS nginx-server

COPY nginx/nginx.conf /etc/nginx/conf.d/default.conf

COPY --from=frontend-builder /app/frontend/dist /usr/share/nginx/html

COPY --from=backend-builder /app /app

RUN apt-get update && apt-get install -y supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

EXPOSE 80
EXPOSE

CMD [ "nginx", "-g", "daemon off;" ]