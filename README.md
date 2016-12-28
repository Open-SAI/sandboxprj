## Setup
- *mkdir myworkfolder*
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

If no errors, go to your web browser and look up the default django url: http://localhost:8000. There is an page error, but is the default configuration, to the url add */crud1* to see the hackenings app (the less buggy experiment in this repo :grin:).

![Preview](https://raw.githubusercontent.com/Open-SAI/sandboxprj/master/preview.png)
Use *ctrl+c* to stop the server, and you can go out from the virtualenv with the *deactivate* command.
