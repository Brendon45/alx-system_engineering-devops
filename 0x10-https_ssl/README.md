# 0x10. HTTPS SSL

## DevOps

## SysAdmin

## Security

![HTTPS](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/276/FlhGPEK.png)

## Background Context

- What happens when you don’t secure your website traffic?

![CONTENT](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/276/xCmOCgw.gif)

## Resources

- Read or watch:

	- [What is HTTPS?](#what-is-https?)
	- [What are the 2 main elements that SSL is providing](#what-are-the-2-main-elements-that-ssl-is-providing)
	- [HAProxy SSL termination on Ubuntu16.04](#haproxy-ssl-termination-on-ubuntu16.04)
	- [SSL termination](#ssl-termination)
	- [Bash function](#bash-function)

## Requirements

## General

	- Allowed editors: vi, vim, emacs
	- All your files will be interpreted on Ubuntu 16.04 LTS
	- All your files should end with a new line
	- A README.md file, at the root of the folder of the project, is mandatory
	- All your Bash script files must be executable
	- Your Bash script must pass Shellcheck (version 0.3.7) without any error
	- The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
	- The second line of all your Bash scripts should be a comment explaining what is the script doing

## Tasks

## 0. World wide web
mandatory
Configure your domain zone so that the subdomain www points to your load-balancer IP (lb-01). Let’s also add other subdomains to make our life easier, and write a Bash script that will display information about subdomains.

Requirements:

- Add the subdomain www to your domain, point it to your lb-01 IP (your domain name might be configured with default subdomains, feel free to remove them)
- Add the subdomain lb-01 to your domain, point it to your lb-01 IP
- Add the subdomain web-01 to your domain, point it to your web-01 IP
- Add the subdomain web-02 to your domain, point it to your web-02 IP
Your Bash script must accept 2 arguments:
1. domain:
- type: string
- what: domain name to audit
mandatory: yes
2. subdomain:
- type: string
- what: specific subdomain to audit
mandatory: no
Output: The subdomain [SUB_DOMAIN] is a [RECORD_TYPE] record and points to [DESTINATION]
When only the parameter domain is provided, display information for its subdomains www, lb-01, web-01 and web-02 - in this specific order
When passing domain and subdomain parameters, display information for the specified subdomain
Ignore shellcheck case SC2086
Must use:
awk
at least one Bash function
You do not need to handle edge cases such as:
Empty parameters
Nonexistent domain names
Nonexistent subdomains

## 1. HAproxy SSL termination
mandatory
“Terminating SSL on HAproxy” means that HAproxy is configured to handle encrypted traffic, unencrypt it and pass it on to its destination.

Create a certificate using certbot and configure HAproxy to accept encrypted traffic for your subdomain www..

Requirements:

	- HAproxy must be listening on port TCP 443
	- HAproxy must be accepting SSL traffic
	- HAproxy must serve encrypted traffic that will return the / of your web server
	- When querying the root of your domain name, the page returned must contain Holberton School
	- Share your HAproxy config as an answer file (/etc/haproxy/haproxy.cfg)
	- The file 1-haproxy_ssl_termination must be your HAproxy configuration file

Make sure to install HAproxy 1.5 or higher, SSL termination is not available before v1.5.
