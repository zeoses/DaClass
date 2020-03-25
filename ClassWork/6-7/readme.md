## install 
```termianl
pip install django
```
## get version of Django
```termianl
python -m django --version
```
## termianl Project
```python
django-admin startproject <NameOFProject>
```

### base Structure of Project
```termianl
─ mysite
   ├── db.sqlite3
   ├── manage.py
   └── mysite
       ├── __init__.py
       ├── __pycache__
       │   ├── __init__.cpython-37.pyc
       │   ├── settings.cpython-37.pyc
       │   ├── urls.cpython-37.pyc
       │   └── wsgi.cpython-37.pyc
       ├── settings.py 
       ├── urls.py
       └── wsgi.py
```

## run Server 
```termianl
python manage.py runserver 
or
./manage.py runserver 
```

# Create App
```termianl
python manage.py startapp <NameOFapp> 
or
./manage.py startapp <NameOFapp>
```
```termianl
├── db.sqlite3
├── manage.py
├── mysite
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-37.pyc
│   │   ├── settings.cpython-37.pyc
│   │   ├── urls.cpython-37.pyc
│   │   └── wsgi.cpython-37.pyc
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── polls
    ├── admin.py
    ├── apps.py
    ├── __init__.py
    ├── migrations
    │   └── __init__.py
    ├── models.py
    ├── tests.py
    └── views.py
```
## MVC ==> MVT

* model : Database
* View : view or object can see user
* Contorler : the logic of Task
---
* model : Database
* view : the logic of Task
* Template : view or object can see user

## TIME ZONE
TIME_ZONE = 'Asia/Tehran'


# useful links 
* [Django Doc](https://docs.djangoproject.com/en/3.0/intro/tutorial01/)
* [Django Girls (Persian)](https://tutorial.djangogirls.org/fa/)