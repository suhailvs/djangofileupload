from django.urls import path
from . import views

urlpatterns = [
    path('', views.UploadView.as_view(), name='fileupload'),
]