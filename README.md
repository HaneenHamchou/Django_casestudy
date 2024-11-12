# Django Case Study

This Django project will create a comprehensive corporate directory where users can create, manage, and view information about corporations.

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)


License: MIT

## Settings

Moved to [settings](https://cookiecutter-django.readthedocs.io/en/latest/1-getting-started/settings.html).

## Basic Steps

### 1. Setting Up the Project

1.	Installing Cookiecutter by “pip install cookiecutter”
2.	Run Cookiecutter with the Django template to create a new projects: “cookiecutter https://github.com/pydanny/cookiecutter-django”
3.	Create virtual environment and activated:<br>
   “python -m venv venv”<br>
   “venv\Scripts\activate”

   
### 2. Create a new Django app
Create the app and include it in INSTALLED_APPS in setting.py

### 3. Develop the Corporation Model
1.  Define corporation model in models.py to represent database tabels with name, address, amd email.
2.  Add a ForeignKey field to relate the Corporations to a User.
3.  Write unit test to verify the Corportions and User Model.

###  4. Create CRUD Templates:
1.  Create HTML templates for create, update and delete corporations in the templates/corp_views directory.
2.  Edit views.py to handle the CRUD operations.

