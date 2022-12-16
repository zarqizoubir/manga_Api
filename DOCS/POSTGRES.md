# Postres Database setup :
-[install pgadmin4](#pgadmin-installation)
- [Linux / MacOs](#linux--macos)
- [Windows](#windows)

-[install postgresql (Server) ](#postgresql-install)

## Pgadmin Installation : 
  - ### Linux / Macos

    A Python package is available for those wishing to run pgAdmin as a web application in a Python environment. Note that the packages do not include the Desktop Runtime.

    pgAdmin is available on PyPi. To install it, create a virtual environment as required, and then use pip to install. Note that pgAdmin will run in server mode, using system-wide paths so you may need to create them first:

    ```shell
    $ sudo mkdir /var/lib/pgadmin
    $ sudo mkdir /var/log/pgadmin
    $ sudo chown $USER /var/lib/pgadmin
    $ sudo chown $USER /var/log/pgadmin
    $ python3 -m venv pgadmin4
    $ source pgadmin4/bin/activate
    (pgadmin4) $ pip install pgadmin4
    ...
    (pgadmin4) $ pgadmin4
    NOTE: Configuring authentication for SERVER mode.

    Enter the email address and password to use for the initial pgAdmin user account:

    Email address: user@domain.com
    Password: 
    Retype password:
    Starting pgAdmin 4. Please navigate to http://127.0.0.1:5050 in your browser.
    * Serving Flask app "pgadmin" (lazy loading)
    * Environment: production
    WARNING: Do not use the development server in a production environment.
    Use a production WSGI server instead.
    * Debug mode: off
    ```

  - ### Windows 
    ```shell
    Docs Will be ready soon
    ```

## Postgresql Install
- Linux Server

    ### Step 1 — Installing PostgreSQL

    To install PostgreSQL, first refresh your server’s local package index:

    ```shell
    sudo apt update
    ``` 

    Then, install the Postgres package along with a -contrib package that adds some additional utilities and functionality:

    ```shell
    sudo apt install postgresql postgresql-contrib
    ``` 

    Ensure that the service is started:

    ```shell
    sudo systemctl start postgresql.service
    ``` 
    ### Step 2 — Using PostgreSQL Roles and Databases
    
    The installation procedure created a user account called postgres that is associated with the default Postgres role. There are a few ways to utilize this account to access Postgres. One way is to switch over to the postgres account on your server by running the following command:

    ```shell
    sudo -i -u postgres
    ``` 

    Then you can access the Postgres prompt by running:
    
    ```shell
    psql
    ``` 
    This will log you into the PostgreSQL prompt, and from here you are free to interact with the database management system right away.

    To exit out of the PostgreSQL prompt, run the following:

    ```shell
    postgres=# \q
    ``` 

    This will bring you back to the postgres Linux command prompt. To return to your regular system user, run the `exit` command:
    
     ```shell
    postgres@server:~$ exit
    ``` 

    Another way to connect to the Postgres prompt is to run the psql command as the postgres account directly with sudo:

    ```shell
    sudo -u postgres psql
    ``` 

    This will log you directly into Postgres without the intermediary `bash` shell in between.

    Again, you can exit the interactive Postgres session by running the following:

    ```shell
    postgres=# \q
    ``` 
    ### Step 3 — Creating a New Role

    If you are logged in as the postgres account, you can create a new role by running the following command:

    ```shell
    postgres@server:~$ createuser --interactive
    ``` 

    If, instead, you prefer to use sudo for each command without switching from your normal account, run:

    ```shell
    sudo -u postgres createuser --interactive
    ``` 

    Either way, the script will prompt you with some choices and, based on your responses, execute the correct Postgres commands to create a user to your specifications.

    ```shell
    Output
    Enter name of role to add: sammy
    Shall the new role be a superuser? (y/n) y
    ```

    ### Step 4 — Creating a New Database

    If you are logged in as the postgres account, you would type something like the following:

    ```shell
     postgres@server:~$ createdb sammy
    ```

    If, instead, you prefer to use sudo for each command without switching from your normal account, you would run:

    ```shell
        sudo -u postgres createdb sammy
    ```

    ### Step 5 — Opening a Postgres Prompt with the New Role

    To log in with ident based authentication, you’ll need a Linux user with the same name as your Postgres role and database.

    If you don’t have a matching Linux user available, you can create one with the adduser command. You will have to do this from your non-root account with sudo privileges (meaning, not logged in as the postgres user):

    ```shell
    sudo adduser sammy
    ```

    Once this new account is available, you can either switch over and connect to the database by running the following:

    ```shell
    sudo -i -u sammy
    psql
    ```

    Or, you can do this inline:

    ```shell
    sudo -u sammy psql
    ```

    This command will log you in automatically, assuming that all of the components have been properly configured.

    If you want your user to connect to a different database, you can do so by specifying the database like the following:

    ```shell
    psql -d postgres
    ```

    Once logged in, you can get check your current connection information by running:

    ```shell
    sammy=# \conninfo
    ```
    ```shell
    Output
    You are connected to database "sammy" as user "sammy" via socket in "/var/run/postgresql" at port "5432".
    ```
    