0x14. MySQL
===========

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/280/KkrkDHT.png)

## Learning Objectives

-   What is the main role of a database
-   What is a database replica
-   What is the purpose of a database replica
-   Why database backups need to be stored in different physical locations
-   What operation should you regularly perform to make sure that your database backup strategy actually works

## Tasks :page_with_curl:

* [4-mysql_configuration_primary](./4-mysql_configuration_primary): The MySQL
`my.conf` configuration file used to set up my first server as a primary database
server on the database `tyrell_corp`.

* [4-mysql_configuration_replica](./4-mysql_configuration_replica): The MySQL
`my.conf` configuration file used to set up my second server as the replica
database server on the database `tyrell_corp`.

* [5-mysql_backup](./5-mysql_backup): Bash script that generates a compressed
`tar.gz` archive from a MySQL dump.
  * Usage: `./5-mysql_backup <MySQL root password>`
  * Generates a dump containing all MySQL databases on the root server.
  * Names the resulting tar archive in the format `day-month-year.tar.gz`.
