from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views as uploader_views

urlpatterns = [
    path('', uploader_views.home, name='imageupload'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)