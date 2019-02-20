Title: Install Node Red Docker behind nginx
Modified: 2018-11-03 15:00
Tags: mqtt, node red, nginx
Summary: Installing Node Red Docker container behind nginx

# Setting up Node Red Docker container behind nginx

## Node Red

[Node Red](https://nodered.org/) has documentation on [running Node Red inside a Docker container](https://nodered.org/docs/platforms/docker).  Should be pretty easy, but I like to wrap my docker container setups into a `docker-compose.yaml` file so it is easier to recreate my docker setup with mapped folders and exposed ports etc.

### `docker-compose.yaml`

~~~
node-red:
  container_name: node-red
  image: nodered/node-red-docker
  restart: always
  ports:
    - "1880:1880/tcp"
  volumes:
    - "/data/node-red:/data"
~~~

## nginx reverse proxy

nignx provides my web front end providing an SSL endpoint to cover all of my web-based services.  To get it to proxy for the Node Red container we need to tweak the config.  Here's the extract from the config file...

~~~
location /node-red/ {
    # Enable authentication
    auth_basic "Login";
    auth_basic_user_file /etc/nginx/passwd;
    # Rewrite the URL
    rewrite ^/node-red/(.*) /$1 break;
    # Pass on the request to node red
    proxy_pass http://localhost:1880;
    proxy_set_header Host $host;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";
}
~~~