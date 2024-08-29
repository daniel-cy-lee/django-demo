Init private_diary project

cmd:
django-admin startproject private_diary


.
└── private_diary
    ├── manage.py
    └── private_diary
        ├── asgi.py
        ├── __init__.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py

3 directories, 6 files


create app

cmd:
py manage.py startapp diary

tree:
create app

cmd:
py manage.py qlite3
├── diary
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── manage.py
└── private_diary
    ├── asgi.py
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-38.pyc
    │   ├── settings.cpython-38.pyc
    │   ├── urls.cpython-38.pyc
    │   └── wsgi.cpython-38.pyc
    ├── settings.py
    ├── urls.py
    └── wsgi.py

5 directories, 18 files

