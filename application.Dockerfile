FROM python:alpine3.18


RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/main" >> /etc/apk/repositories


# Install Python and pip
RUN apk add --update  mariadb-connector-c-dev build-base pkgconf unixodbc-dev
RUN pip3 install --no-cache --upgrade pip setuptools


# Set the working directory
WORKDIR /empire

# Copy the application files
COPY ./api ./api
COPY ./setup ./setup
COPY ./models ./models

# Install Python dependencies
WORKDIR /empire/setup
RUN pip install --upgrade setuptools wheel
RUN pip install --upgrade maturin
RUN pip install -r requirements.txt
RUN apk add --update

RUN pip install mysqlclient
RUN pip install gunicorn
# Switch back to the main directory
WORKDIR /empire

CMD ["python3", "api.v1.app"]
