from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', PostList.as_view(), name="blog"),
    url(r'^search-results/$', SearchContent.as_view(), name='search-results'),
    url(r'^category/(?P<slug>\S+)$', CategoryDetail.as_view(), name='category'),
    url(r'^tags/(?P<slug>\S+)$', TagsList.as_view(), name="tags"),
    url(r'^(?P<slug>\S+)$', PostDetail.as_view(), name='post'),

]

