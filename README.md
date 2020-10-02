# django-starter

This is Django Rest Framework based starter application having following implementation

1. Registration API
2. Login API : JWT based authentication and authroization
3. User API
4. ToDo API 
    1. Admin can view all the ToDo list
    2. User can view their own ToDO list
5. Swagger implementation for API documentation and Testing
6. Custom Group
7. Custom permissions 

**Django pacckages used in this projects are** 

I have used python3.8 for the development environment

1. $ pip install django
2. $ pip install djangorestframework==3.11
3. $ pip install djangorestframework-jwt
4. $ pip install mysqlclient
5. $ pip install drf_yasg
6. $ pip install wheel
7. $ pip install django-rest-auth

**Setup & Run**

1. Create virtual environment 
    https://docs.python.org/3/tutorial/venv.html
2. Install all the necessary packages mentioned above
3. Make changes to config/settings.py for required mysql database changes
    https://docs.djangoproject.com/en/3.1/ref/databases/
4. Run following commands for database migrations script and create superuser in application home directory
    
    ` $ python manage.py makemigrations`
    ` $ python manage.py migrate`
    ` $ python manage.py createsuperuser`

5. Run the application
    ` $ python manage.py runserver 0.0.0.0:3000`


# ToDo
1. Email Service
2. Token based email verification
3. Forgot and Reset Password API


    
