# Introduction

This is a course on developing with django using a [pluralsight course](https://app.pluralsight.com/course-player?clipId=08e4d747-4a0e-4216-b614-9a3160f38690) . The documentation for Django can be found @ https://docs.djangoproject.com/en/3.1/

Get started by:

- If you have the full version of Pycharm, start with the django template
- Creating a **new Python project** in *Pycharm* community then create an empty python project and then inititalising it with `python -m pip install django` 
  - `django-admin startproject  <ProjectName>` for creating a new project
- `python manage.py runserver` to run the project
- The full course can be found at [django_getting_started](https://github.com/codesensei-courses/django_getting_started)
- Create another folder `python manage.py startapp <folder or domain name>`
- `python manage.py showmigrations` shows migrations not yet set and `python manage.py migrate` migrates the changes
- `python manage.py dbshell` show **sqlite** db entries but it is easier through pycharm database console
- `python manage.py makemigrations` generates a migration based on the model created and needs this to be setup in the applications
- `python manage.py sqlmigrate <modelname> <version>` will migrate the sql generated from the migration
- ` python manage.py migrate` generates the migration into the database
- `python manage.py createsuperuser` to create an **admin** for the site which works on the http://localhost:8000/admin URL
- Django model fields and setting up the models can be found https://docs.djangoproject.com/en/3.1/ref/models/fields/

