# CRUD Operation using Django for two tables of PostgreSQL Database
> CRUD operation in Django+PostgreSQL Database for two Tables

## The Steps:

### 1. Open PSQL terminal and Enter the followings....
`
Server [localhost]: localhost <br>
Database [postgres]: PgsDBtoPy <br>
Port [5432]: 5432 <br>
Username [postgres]: innovapgs <br>
Password for user innovapgs: tables2@py
`


### 2. Create tables (name: Customer and Invoice)

PgsDBtoPy=# <br>
```
create table if not exists customer (customer_id SERIAL PRIMARY KEY, customer_name VARCHAR(100) NOT NULL, room_no integer NOT NULL DEFAULT '1', checkin_date DATE NOT NULL, checkout_date DATE NOT NULL); <br>
```

And <br>

PgsDBtoPy=# <br>
```
create table if not exists invoice (bill_id SERIAL PRIMARY KEY, customer_id integer NOT NULL, customer_name VARCHAR(100), bill_date DATE NOT NULL, amount_paid float4 NOT NULL);
```


### 3. Check the Tables: 
PgsDBtoPy=# \dt


### 4. In Django Settings.py:
`
DATABASES = { <br>
    'default': { <br>
       'ENGINE': 'django.db.backends.postgresql', <br>
       'NAME': 'PgsDBtoPy', <br>
       'USER': 'innovapgs', <br>
       'PASSWORD': 'tables2@py', <br>
       'HOST': '127.0.0.1', <br>
       'PORT': '5432', <br>
    } <br>
}
`


### 5. Inspect Database to Django Model:

`py manage.py inspectdb > models_new.py` <br>


Rename models_new.py to models.py <br>
And save it to under myApp.



### 6. Migration: 
+  `py manage.py makemigrations` <br>

+  `py manage.py sqlmigrate myApp 0001` <br>

+  `py manage.py migrate` <br>


### 7. Edit the Settings, URLs and Views in Django

