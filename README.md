# simple django imageupload(django 3.x)

## Run locally

### 1. Set Environment file `.env` in project directory:

    SECRET_KEY=xxxx
    DATABASE_URL=
    AWS_ACCESS_KEY_ID=xxxx
    AWS_SECRET_ACCESS_KEY=xxxx


### 2. Syncronize database

    $ python manage.py migrate
    $ python manage.py runserver

visit <http://localhost.com:8000/>


# Heroku

+ create and app at https://dashboard.heroku.com/apps/
+ click `Deploy` Tab -> Deploy method `Github`
+ Manual deploy, select `heroku` branch, click `Deploy Branch`
+ Install heroku `$ sudo snap install --classic heroku`
+ logs `$ heroku logs -a djangofileupload` 
+ `$ heroku run -a djangofileupload python manage.py migrate`
