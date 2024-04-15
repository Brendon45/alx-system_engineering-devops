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
