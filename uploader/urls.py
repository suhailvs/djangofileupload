from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.UploadView.as_view(), name='fileupload'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)