from django.db import models
from django.forms import ModelForm

class Upload(models.Model):
	pic = models.FileField(upload_to="images/")    
	upload_date=models.DateTimeField(auto_now_add =True)

# FileUpload form class.
class UploadForm(ModelForm):
	class Meta:
		model = Upload
		fields = ('pic',)