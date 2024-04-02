# 0x0E. Web stack debugging #1

## DevOps

## SysAdmin

## Scripting

## Debugging

![DEBUGG](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/271/B4eeypV.jpg)

## Requirements

## General

	- Allowed editors: vi, vim, emacs
	- All your files will be interpreted on Ubuntu 20.04 LTS
	- All your files should end with a new line
	- A README.md file at the root of the folder of the project is mandatory
	- All your Bash script files must be executable
	- Your Bash scripts must pass Shellcheck without any error
	- Your Bash scripts must run without error
	- The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
	- The second line of all your Bash scripts should be a comment explaining what is the script doing
	- You are not allowed to use wget

## Tasks

## 0. Nginx likes port 80
- mandatory
Using your debugging skills, find out what’s keeping your Ubuntu container’s Nginx installation from listening on port 80. Feel free to install whatever tool you need, start and destroy as many containers as you need to debug the issue. Then, write a Bash script with the minimum number of commands to automate your fix.

Requirements:

- Nginx must be running, and listening on port 80 of all the server’s active IPv4 IPs
- Write a Bash script that configures a server to the above requirements

## 1. Make it sweet and short
#advanced
Using what you did for task #0, make your fix short and sweet.

Requirements:

	- Your Bash script must be 5 lines long or less
	- There must be a new line at the end of the file
	- You must respect usual Bash script requirements
	- You cannot use ;
	- You cannot use &&
	- You cannot use wget
	- You cannot execute your previous answer file (Do not include the name of the previous script in this one)
	service (init) must say that nginx is not running ← for real
