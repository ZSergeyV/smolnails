from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^authorize-instagram$', Authorize_Instagram, name="authorize"),
    url(r'^instagram$', Instagram, name="instagram"),
    ]

