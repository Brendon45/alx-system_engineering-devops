# 0x13. Firewall

## DevOps

## SysAdmin

## Security

![SECURITY](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/284/V1HjQ1Y.png)

## Background Context

- Your servers without a firewall…
![SECURITY](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/155/holbertonschool-firewall.gif)

## Resources

- Read or watch:

	- [What is a firewall](#what-is-a-firewall)

## Warning!

- Containers on demand cannot be used for this project (Docker container limitation)

- Be very careful with firewall rules! For instance, if you ever deny port 22/TCP and log out of your server, you will not be able to reconnect to your server via SSH, and we will not be able to recover it. When you install UFW, port 22 is blocked by default, so you should unblock it immediately before logging out of your server.

## Tasks

## 0. Block all incoming traffic but
mandatory

- Let’s install the ufw firewall and setup a few rules on web-01.

Requirements:

- The requirements below must be applied to web-01 (feel free to do it on lb-01 and web-02, but it won’t be checked)
- Configure ufw so that it blocks all incoming traffic, except the following TCP ports:
	- 22 (SSH)
	- 443 (HTTPS SSL)
	- 80 (HTTP)
- Share the ufw commands that you used in your answer file

Repo:

	- GitHub repository: alx-system_engineering-devops
	- Directory: 0x13-firewall
	- File: 0-block_all_incoming_traffic_but

## 1. Port forwarding
#advanced

Firewalls can not only filter requests, they can also forward them.

Requirements:

- Configure web-01 so that its firewall redirects port 8080/TCP to port 80/TCP.
- Your answer file should be a copy of the ufw configuration file that you modified to make this happen
Terminal in web-01:

- listen 8000;
- listen somename:8080;
- listen 443;

root@03-web-01:~#

- My web server nginx is only listening on port 80
- netstat shows that nothing is listening on 8080

Terminal in web-02:

ubuntu@03-web-02:~$ curl -sI web-01.holberton.online:80

HTTP/1.1 200 OK

Server: nginx/1.4.6 (Ubuntu)

Date: Tue, 07 Mar 2017 02:14:41 GMT

Content-Type: text/html

Content-Length: 612

Last-Modified: Tue, 04 Mar 2014 11:46:45 GMT

Connection: keep-alive

ETag: "5315bd25-264"

Accept-Ranges: bytes

ubuntu@03-web-02:~$ curl -sI web-01.holberton.online:8080
HTTP/1.1 200 OK

Server: nginx/1.4.6 (Ubuntu)

Date: Tue, 07 Mar 2017 02:14:43 GMT

Content-Type: text/html

Content-Length: 612

Last-Modified: Tue, 04 Mar 2014 11:46:45 GMT

Connection: keep-alive

ETag: "5315bd25-264"

Accept-Ranges: bytes

ubuntu@03-web-02:~$

- I use curl to query web-01.holberton.online, and since my firewall is forwarding the ports, I get a HTTP 200 response on port 80/TCP and also on port 8080/TCP.

Repo:

	- GitHub repository: alx-system_engineering-devops
	- Directory: 0x13-firewall
	- File: 100-port_forwarding
