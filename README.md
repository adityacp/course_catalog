Course Catalog
==============

Introduction
============

A Course Catalog for showing different types of courses.
Try out the demo at https://demoapp-c147d.appspot.com/

Requirements
============

- Python 3.8
- Django 3.2.12

**Installation and Setup**

- Installing system requirements
      
  **Any Operating System**
       
       Install Python and create a virtual env. You can use this link for reference https://docs.python.org/3/library/venv.html. Also, anaconda can be used for the setup.
      
-  Clone the repository

       git clone https://github.com/adityacp/course_catalog.git

-  Go to the project directory

       cd course_catalog


- Installing project packages

      pip install -r requirements.txt


- Run migrations

      python manage.py migrate

- Create superuser

      python manage.py createsuperuser

- Run server Locally

      python manage.py runserver

- Once the backend server is running, follow the steps below to compile the frontend UI.
     
      cd frontend
     
      and then follow the steps mentioned in https://github.com/adityacp/course_catalog/tree/main/frontend


- Create new entries

      Go to 127.0.0.1:8000/admin and use the credentials created with step 6 i.e. Create Superuser
      
      In AUTHENTICATION AND AUTHORIZATION section click on the user to create new users.
      
      In the BACKEND section two links will be available Categorys and Courses. Click on the links to create the categories and courses. To create a course it is mandatory to         create a category first.

- Connecting to Dashboard

      Go to 127.0.0.1:8000/ to view the UI
