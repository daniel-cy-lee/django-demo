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
    ├── settings.py  
    ├── urls.py  
    └── wsgi.py  

5 directories, 18 files

TODO:   
implement Page 22 - 27  

下載模板  
django/private_diary   
.  
├── diary  
│   └── templates  
├── private_diary  
└── static  
    ├── assets  
    │   └── img  
    ├── css  


[Add mystock app]  
django-admin startapp mystock  
  
~/django/private_diary $ tree -d -I  __pycache__  
.  
├── diary  
│   ├── migrations  
│   └── templates  
├── mystock  
│   └── migrations  
├── private_diary  
└── static  
    ├── assets  
    │   └── img  
    ├── css  
    └── js  
  
$ tree mystock/  
mystock/  
├── admin.py  
├── apps.py  
├── __init__.py  
├── migrations  
│   └── __init__.py  
├── models.py  
├── tests.py  
└── views.py  
