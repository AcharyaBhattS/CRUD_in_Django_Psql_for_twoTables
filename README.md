# CRUD_Django_Psql_for_twoTables
CRUD operation in Django+PostgreSQL Database for two Tables

## The Steps:

# 1. Open PSQL terminal and Enter the followings....

Server [localhost]: localhost
Database [postgres]: PgsDBtoPy
Port [5432]: 5432
Username [postgres]: innovapgs
Password for user innovapgs: tables2@py

# 2. # To Check the Table list....   
PgsDBtoPy=# \dt

# 3. Create tables (name: Customer and Invoice)

PgsDBtoPy=# create table if not exists customer (customer_id SERIAL PRIMARY KEY, customer_name VARCHAR(100) NOT NULL, room_no integer NOT NULL DEFAULT '1', checkin_date DATE NOT NULL, checkout_date DATE NOT NULL);

PgsDBtoPy=# create table if not exists invoice (bill_id SERIAL PRIMARY KEY, customer_id integer NOT NULL, customer_name VARCHAR(100), bill_date DATE NOT NULL, amount_paid float4 NOT NULL);


# 4. PgsDBtoPy=# \dt


# 5. In Django Settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'PgsDBtoPy',
        'USER': 'innovapgs',
        'PASSWORD': 'tables2@py',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


# 6. Inspect Database to Django Model:
py manage.py inspectdb > models_new.py

Rename models_new.py to models.py 
And save it to under myApp.

# 7. py manage.py makemigrations

# 8. py manage.py sqlmigrate myApp 0001

# 9. py manage.py migrate

# 10. Edit Settings, URLs, Views

