# simple django imageupload(django 1.11)

## usage

**On `setting.py` add:**

	INSTALLED_APPS = (
		...
		'uploader',		
	)
	MEDIA_ROOT = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'media')
	MEDIA_URL = '/media/'

**On `urls.py` append:**	
	
	...<other imports>...
	from django.conf import settings
	from django.conf.urls.static import static
	from uploader import views as uploader_views
	
	urlpatterns = [
		...<other url patterns>...
		url(r'^upload/$', uploader_views.home, name='imageupload'),
	]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

**Syncronize database and runserver**

	>> python manage.py makemigrations
	>> python manage.py migrate
	>> python manage.py runserver

	visit <http://localhost.com:8000/upload>