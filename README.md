# simple django imageupload

## Start a sample django project: `django-admin.py startproject sample` 

### now a folder(`sample`) with these files are created:
	
	sample/
		manage.py
		sample/
			__init__.py
			settings.py
			urls.py
			wsgi.py	

### Download this repo and copy the folder `uploader` into the directory contains `manage.py`.

### On `setting.py` add:  

	INSTALLED_APPS = (
		...
		'uploader',
		...
	)
	MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
	MEDIA_URL = '/media/'

### On `urls.py` add:

	...<other imports>...
	from django.conf import settings
	from django.conf.urls.static import static
	
	urlpatterns = patterns('',
		url(r'^upload/$', 'uploader.views.home', name='imageupload'),
		...<other url patterns>...
	)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

### Syncronize database and runserver:
	
	python manage.py syncdb
	python manage.py runserver

## `uploader` app:

### Structure

	uploader/
		__init__.py
		models.py
		views.py			
		templates/
			home.html

### models.py

	from django.db import models
	from django.forms import ModelForm

	class Upload(models.Model):
	    pic = models.ImageField("Image", upload_to="images/")    
	    upload_date=models.DateTimeField(auto_now_add =True)

	# FileUpload form class.
	class UploadForm(ModelForm):
		class Meta:
			model = Upload

### views.py

	from django.shortcuts import render
	from uploader.models import UploadForm,Upload
	from django.http import HttpResponseRedirect
	from django.core.urlresolvers import reverse
	# Create your views here.
	def home(request):
		if request.method=="POST":
			img = UploadForm(request.POST, request.FILES)		
			if img.is_valid():
				img.save()	
				return HttpResponseRedirect(reverse('imageupload'))
		else:
			img=UploadForm()
		images=Upload.objects.all()
		return render(request,'home.html',{'form':img,'images':images})

### templates/home.html

	<div style="padding:40px;margin:40px;border:1px solid #ccc">
		<h1>picture</h1>
		<form action="#" method="post" enctype="multipart/form-data">
			{% csrf_token %} {{form}} 
			<input type="submit" value="Upload" />
		</form>
		{% for img in images %}
			{{forloop.counter}}.<a href="{{ img.pic.url }}">{{ img.pic.name }}</a>
			({{img.upload_date}})<hr />
		{% endfor %}
	</div>