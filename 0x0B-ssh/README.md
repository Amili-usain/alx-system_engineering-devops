0x0B. SSH
=========

Background Context
------------------

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/244/zPVRKhPsUP5lK.gif)

Along with this project, you have been attributed an Ubuntu server, living in a datacenter far far away. Like level 2 of the application process, you will connect using `ssh`. But contrary to level 2, you will not connect using a password but an RSA key. We've configured your server with the public key you created in the first task of [a previous project](https://alx-intranet.hbtn.io/rltoken/UQIQV4HJGvBv0qrHhlDFaQ "a previous project") shared in your [intranet profile](https://alx-intranet.hbtn.io/rltoken/8ZlNV0J-sa-dijhmhJolOg "intranet profile").

You can access your server information in the [my servers](https://alx-intranet.hbtn.io/rltoken/e2_s_pXwBVuYbhrvoesfrg "my servers") section of the intranet, each line with contains the IP and username you should use to connect via `ssh`.

**Note:** Your server is configured with an Ubuntu 20.04 LTS environment.

Learning Objectives
-------------------

At the end of this project, you are expected to be able to [explain to anyone](https://alx-intranet.hbtn.io/rltoken/0Wgw_i87NIVCfUcRzdZgkg "explain to anyone"), **without the help of Google**:

### General

-   What is a server
-   Where servers usually live
-   What is SSH
-   How to create an SSH RSA key pair
-   How to connect to a remote host using an SSH RSA key pair
-   The advantage of using `#!/usr/bin/env bash` instead of `/bin/bash`

## Files

| Filename | Description |
| -------- | ----------- |
| `0-use_a_private_key` | Uses `ssh` to connect to a server using a private key previously generated |
| `1-create_ssh_key_pair` | Creates an RSA key pair |
| `2-ssh_config` | SSH client configuration using a private key and refusing to authenticate using a password |
| `100-puppet_ssh_config.pp` | Sets up the client SSH configuration file to connect to a server without typing a password |
