# DJANGO Application for sending SMS

## Explanation

This assignment is a Django-based SMS application designed to manage SMS communications. It provides users with a simple interface for managing SMS campaigns efficiently.

To set up the application: First we created a new Django project before setting up a dashboard app for managing user interactions then registered the app in settings.py by adding dashboard to the installed_apps list before running the server. 

Perform initial migrations to set up the authentication and user model. Create a superuser account to access the Django admin interface. In models.py of the dashboard app, define a message model before migrating and register the model in admin.

We also sign up for a Twilio account to complete the email verification and phone number confirmation process and install twilio library before integrating twilio api by setting up the Twilio client using the account SID and auth token to use environment variables for security then override the save method to send SMS when the score is 70 or above.

We added a virtual environment(venv) called myvenv to install django packages

To run the application: in the terminal type **.\myvenv\Scripts\activate** to activate the virtual environment 
after that we run **python manage.py runserver** and the django server will be given, then we add **admin** to the server http://127.0.0.1:8000 in order to login in the admin page and it should look like this **http://127.0.0.1:8000/admin/**
