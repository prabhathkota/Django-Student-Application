Steps to install Student Application
#######################################
django-admin.py startproject StudentWebsite
python manage.py startapp StudentApp
python manage.py validate
python manage.py sqlall StudentApp

MySQL Database Details
#########################
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'studentsdb',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'XXXX',
        'PASSWORD': 'XXXX',
        'HOST': '127.0.0.1',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '3306',                      # Set to empty string for default.
    }
}

JavaScript Modules:
####################

Highcharts
http://code.highcharts.com/modules/exporting.js
http://code.highcharts.com/highcharts.js

Jquery
http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js

Insert MySQL sample data
##########################
Load "studentapp.sql" into database

Models Used:
#############
Student
Subject
StudentMarks


How to start Django Development Server
#######################################
Django develeopment server works on default port 8000
python manage.py runserver 8000 

Access Home Page
#################
http://127.0.0.1:8000/home/

