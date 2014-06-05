# simple django imageupload

## usage

**On `setting.py` add:**

	INSTALLED_APPS = (
		...
		'uploader',		
	)
	MEDIA_ROOT = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'media')
	MEDIA_URL = '/media/'

**On `urls.py` append:**	
	
	...
	from django.conf import settings
	from django.conf.urls.static import static

	urlpatterns += patterns('uploader.views',
		url(r'^$', 'home', name='imageupload'),	
	)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
