# 0x0B. SSH

## DevOps
## SSH
## SysAdmin
## Security

## Learning Objectives

- At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

## General

- What is a server
- Where servers usually live
- What is SSH
- How to create an SSH RSA key pair
- How to connect to a remote host using an SSH RSA key pair
- The advantage of using #!/usr/bin/env bash instead of /bin/bash

## ANSWERS

- What is a server?

A server is a computer program or device that provides functionality or resources to other programs or devices, known as clients, over a network. In simple terms, it's a computer system designed to provide data, services, or functionality to other computers or clients on a network.

- Where servers usually live?

Servers can physically reside in data centers or server rooms within an organization's premises. They can also be hosted remotely in the cloud, provided by cloud service providers like Amazon Web Services (AWS), Google Cloud Platform (GCP), or Microsoft Azure.

- What is SSH?

SSH, or Secure Shell, is a cryptographic network protocol used for securely accessing and managing remote servers over an unsecured network. It provides a secure, encrypted connection between a client and a server, allowing users to execute commands, transfer files, and perform other network-related tasks securely.

- How to create an SSH RSA key pair?

After generating the SSH key pair, you can copy the public key to the remote server's ~/.ssh/authorized_keys file. Then, you can use the ssh command to connect to the remote host:
- code
ssh username@remote_host

- The advantage of using #!/usr/bin/env bash instead of /bin/bash

Using #!/usr/bin/env bash at the beginning of a script allows the system to locate the Bash interpreter (bash) dynamically using the env command, which searches the system's PATH environment variable. This approach is more flexible because it doesn't hardcode the interpreter's path (/bin/bash), making the script more portable across different systems where Bash may be installed in different locations.

N.B - If the SSH key pair is correctly configured, it will allow you to authenticate without entering a password.

## Requirements

## General

- Allowed editors: vi, vim, emacs
- All your files will be interpreted on Ubuntu 20.04 LTS
- All your files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
- The second line of all your Bash scripts should be a comment explaining what is the script doing

## Tasks

0. Use a private key
mandatory
Write a Bash script that uses ssh to connect to your server using the private key ~/.ssh/school with the user ubuntu.

Requirements:

Only use ssh single-character flags
You cannot use -l
You do not need to handle the case of a private key protected by a passphrase

1. Create an SSH key pair
mandatory
Write a Bash script that creates an RSA key pair.

Requirements:

Name of the created private key must be school
Number of bits in the created key to be created 4096
The created key must be protected by the passphrase betty

2. Client configuration file
mandatory
Your machine has an SSH configuration file for the local SSH client, let’s configure it to our needs so that you can connect to a server without typing a password. Share your SSH client configuration in your answer file.

Requirements:

Your SSH client configuration must be configured to use the private key ~/.ssh/school
Your SSH client configuration must be configured to refuse to authenticate using a password

3. Let me in!
mandatory
Now that you have successfully connected to your server, we would also like to join the party.

Add the SSH public key below to your server so that we can connect using the ubuntu user.

4. Client configuration file (w/ Puppet)
#advanced
Let’s practice using Puppet to make changes to our configuration file. Just as in the previous configuration file task, we’d like you to set up your client SSH configuration file so that you can connect to a server without typing a password.

Requirements:

Your SSH client configuration must be configured to use the private key ~/.ssh/school
Your SSH client configuration must be configured to refuse to authenticate using a password

Happy Coding!
