from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', Gallery.as_view(), name="gallery"),
    url(r'^(?P<slug>\S+)$', AlbumView.as_view(), name='album'),
]

