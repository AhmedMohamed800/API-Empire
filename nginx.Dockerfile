FROM nginx:alpine


RUN apk add python3-dev py3-pip build-base libressl-dev musl-dev libffi-dev
RUN pip3 install pip --upgrade
RUN pip3 install cerbot-nginx
RUN mkdir /etc/letsencrypt
COPY default.conf /etc/nginx/conf.d/default.conf


RUN certbot --nginx -d apiempire.site -d www.apiempire.site
