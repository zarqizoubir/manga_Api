# Link The Postgress Database with django :

- The requirements 

    we need to install an adapter for postgres ```psycopg2``` by runing :

    ```shell
    pip install psycopg2-binary
    ```

- add The new database configuration

    delete the old configuration
    
    ```python
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
    ```

    add add the new one :
    
    ### fill the data between the brackets with yours 
    
    ```python
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': [Database Name],
        'USER': [USERNAME],
        'PASSWORD': [PASSWORD],
        'HOST': [HOST],
        'PORT': [PORT],
        }
    }
    ```

- Setup with the models :

    after linking the database you may need to run the migration :

    ```shell
    python3 manage.py migrate
    ```


### and Never Stop Learning [HERE](google.com)