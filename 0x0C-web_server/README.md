# 0x0C. Web server

## DevOps

## SysAdmin

![WEBSERVER](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/266/8Gu52Qv.png)

## Background Context

In this project, some of the tasks will be graded on 2 aspects:
- Is your web-01 server configured according to requirements
- Does your answer file contain a Bash script that automatically performs commands to configure an Ubuntu machine to fit requirements (meaning without any human intervention)

For example, if I need to create a file /tmp/test containing the string hello world and modify the configuration of Nginx to listen on port 8080 instead of 80, I can use emacs on my server to create the file and to modify the Nginx configuration file /etc/nginx/sites-enabled/default.

But my answer file would contain:

sylvain@ubuntu cat 88-script_example
#!/usr/bin/env bash
# Configuring a server with specification XYZ
echo hello world > /tmp/test
sed -i 's/80/8080/g' /etc/nginx/sites-enabled/default
sylvain@ubuntu

As you can tell, I am not using emacs to perform the task in my answer file. This exercise is aiming at training you on automating your work. If you can automate tasks that you do manually, you can then automate yourself out of repetitive tasks and focus your energy on something more interesting. For an SRE, that comes very handy when there are hundreds or thousands of servers to manage, the work cannot be only done manually. Note that the checker will execute your script as the root user, you do not need to use the sudo command.

![DOCKER](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/266/82VsYEC.jpg)

- Tips: to test your answer Bash script, feel free to reproduce the checker environment:
-  start a Ubuntu 16.04 sandbox
-  run your script on it
-  see how it behaves

## Resources

- Read or watch:
- [How the web works](#how-the-web-works)
- [Nginx](#nginx)
- [How to Configure Nginx](#how-to-configure-nginx)
- [Child process concept page](#child-process-concept-page)
- [Root and sub domain](#root-and-sub-domain)
- [HTTP requests](#http-requests)
- [HTTP redirection](#http-redirection)
- [Not found HTTP response code](#not-found-http-response-code)
- [Logs files on Linux](#logs-files-on-linux)

## Requirements

## General
-  Allowed editors: vi, vim, emacs
-  All your files will be interpreted on Ubuntu 16.04 LTS
-  All your files should end with a new line
-  A README.md file, at the root of the folder of the project, is mandatory
-  All your Bash script files must be executable
-  Your Bash script must pass Shellcheck (version 0.3.7) without any error
-  The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
-  The second line of all your Bash scripts should be a comment explaining what is the script doing
-  You can’t use systemctl for restarting a process
