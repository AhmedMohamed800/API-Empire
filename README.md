# API Empire

Api Empire is a platform that provides various APIs for developers through subscription-based services.

## Table of Contents

1. [Teconologies](#teconologies)
2. [How to Run the Application](#run)
3. [Team](#team)

## Teconologies

### Front-end

- ReactJS: JavaScript library for building user interfaces.
- Typescript: Typed JavaScript with static checking.
- Tailwind CSS: Open-source CSS framework.
- Library:
  - react-router-dom: Declarative routing for React.js.
  - zustand: State management.
  - @paypal/react-paypal-js: integrate paypal with react
  - axios: Promise-based HTTP client for JavaScript.

### Back-end

- Flask: Micro web framework in Python.
- MySQL: Open-source relational database management system.
- Library:
  - flask-cors: Cross-origin resource sharing (CORS) for Flask.
  - flask_mail: Send email from Flask applications.
  - sqlalchemy: Python SQL toolkit and ORM.
  - paypalrestsdk: PayPal API client for Python.
  - mysql: MySQL driver for Python.
  - uuid: Generate UUIDs.

### Web Server

- Nginx: Open-source reverse proxy server for HTTP, HTTPS, SMTP, POP3, and IMAP protocols.
- Gunicorn: Python WSGI HTTP Server for UNIX.

## How to Run the Application

### 1. server:

- Navigate to **setup** directory.
- Run `./setup.sh` to install all dependencies.
- Write the follwing command to setup the database:

  ```bash
  cat db.sql | mysql -u root -p
  ```

- Run `./script.py` to seed the database with data.
- Configure Nginx to proxy pass to Gunicorn on port 5002.

### 2. Front-end:

- Navigate to the **frontend** directory then add .env in file in src with following details:
  - REACT_APP_API_URL
  - REACT_APP_PAYPAL_CLIENT_ID
- Run the following in the terminal:

  ```bash
  npm run build
  ```

- Copy the content of **dist** folder to the **api/build** directory.

### 3. Back-end:

- Navigate to the root directory.
- Write the following command to run the application:

  ```bash
  tmux new-session -d 'gunicorn --bind 0.0.0.0:5002 api.v1.app:app'
  ```

## Team

### 1. Ahmed Mohamed Ahmed Abdou:

- Responsible for designing the user interface and writing front-end code.

### 2. Abdelrhman (DINAMOW) Abdelhameed:

- Responsible for designing the database, configuring the server, and developing the back end.
