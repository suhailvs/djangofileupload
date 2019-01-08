# simple django imageupload(django 2.x)

## [demo](https://djangofileupload.herokuapp.com/uploader/)

## usage

### 1. Download the folder `uploader`:

Download the folder `uploader` and save it in your project directory.

### 2. Update `setting.py` of your project:

On `setting.py` add:

    INSTALLED_APPS = [
        ...<other apps>...
        'uploader.apps.UploaderConfig',
    ]

    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    MEDIA_URL = '/media/'

### 3. Update `urls.py` of your project:

On `urls.py` add:   
    
    ...<other imports>...
    from django.urls import path,include
    
    urlpatterns = [
        ...<other url patterns>...
        path('uploader/', include('uploader.urls'))
    ]

### 4. Syncronize database

    $ python manage.py makemigrations
    $ python manage.py migrate
    $ python manage.py runserver

visit <http://localhost.com:8000/uploader>
