FROM nginx:alpine


RUN apk add python3-dev py3-pip build-base libressl-dev musl-dev libffi-dev
RUN pip3 install pip --upgrade
RUN pip3 install certbot-nginx 
RUN mkdir /etc/letsencrypt

# Copy the Nginx configuration file and proxy_params file into the Docker image
COPY default.conf /etc/nginx/conf.d/default.conf
COPY proxy_params /etc/nginx/proxy_params
RUN certbot --nginx --email ahmedmoh0107@gmail.com --agree-tos --non-interactive -d app.apiempire.site 

CMD ["nginx", "-g", "daemon off;"]
