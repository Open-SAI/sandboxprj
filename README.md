## Red Hat based Linux distros (Tested with CentOS 7, Fedora 24)

## Setup
- *mkdir myworkfolder*
- *cd myworkfolder*
- *git clone https://github.com/Open-SAI/sandboxprj.git*

It create a *sandboxprj* folder in your *myworkfolder*, we need the python environment and to install django and other tools:

1. First as admin (in Fedora 24):
 - *dnf install python3-virtualenv* (15.0.3-2.fc24)
 - *dnf install python3-pip*  (8.0.2-1.fc24)
2. Next as normal user in our *myworkfolder* created previously:
 - *virtualenv-3.5 --python=python3.5 sandboxenv*
 - *source sandboxenv/bin/activate*
 - *pip install django~=1.10.0*
 - *pip install django-datetime-widget*
 - *cd sandboxprj*
 - *python manage.py migrate*
 - *python manage.py runserver*


## Debian based Linux distros

## Setup

- *$ mkdir /../myworkfolder/*
- *$ cd myworkfolder*
- *$ git clone https://github.com/Open-SAI/sandboxprj.git*

It create a *sandboxprj* folder in your *myworkfolder*, we need the python environment and to install django and other tools:

1. First as admin/root:

 - *$ apt install python3*
 - *$ apt install python3-pip*
 - *$ pip3 install virtualenv*

2. Next as normal user in our "myworkfolder" created previously:
 - *$ virtualenv /../myworkfolder/*
 - *$ cd myworkfolder*
 - *$ source /bin/activate*
 - *$ pip3 install Django*
 - *$ pip3 install django-datetime-widget*
 - *$ cd sandboxprj*
 - *$ python manage.py migrate*
 - *$ python manage.py runserver*


## If no errors...
Go to your web browser and look up the default django url: http://localhost:8000. There is an page listing the url's to the apps from the sandboxprj project (and the admin interface). The CRUD - */crud1* is the hackening app (the less buggy experiment in this repo :grin:).

![Preview](https://raw.githubusercontent.com/Open-SAI/sandboxprj/master/preview.png)
Use *ctrl+c* to stop the server, and you can go out from the virtualenv with the *deactivate* command.

