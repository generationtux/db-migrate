# db-migrate

Migrate a MySQL database from one host to another host.

## Using db-migrate

A vagrant file is provided that will allow you to build an Ubuntu Wiley 64 box
which you can use to run db-migrate.

### Build Vagrant

-   `cd path/to/db-migrate/devel`

-   `vagrant up devel`  
    This will build the development vagrant box

-   Go to the development directory:  
    `cd /development`

-   `chmod +x build.sh && ./build.sh`  
    This will "build" the Python script to an executable file

-   To use dbmigrate:  
`dbmigrate --src 127.0.0.1 username database --dest 127.0.0.1 username`  
The following information must be provided and in this order:

    -   Source DB Hostname/IP (i.e. 127.0.0.1)
    -   Source DB Username
    -   Source DB Database
    -   Destination DB Hostname
    -   Destination DB Username *(must have database creat privileges)*
