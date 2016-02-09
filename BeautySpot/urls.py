
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.http import HttpResponse
from BS.views import Index, Contacts, ReservationForm, Reservation
from django.views.decorators.cache import cache_page
from django.contrib.sitemaps.views import sitemap
from .sitemap import PostSitemap, CategorySitemap, ServiceSitemap, AlbumsSitemap,HomeSitemap
from BS.services.feeds import ServicesFeed


sitemaps = {
    'home':HomeSitemap,
    'articles':PostSitemap,
    'category':CategorySitemap,
    'service':ServiceSitemap,
    'gallery':AlbumsSitemap
}


urlpatterns = [
    url(r'^$', cache_page(60 * 15)(Index.as_view()), name="index"),
    #url(r'^social/',include('BS.social.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^services/', include('BS.services.urls')),
    url(r'^gallery/', include('BS.gallery.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('BS.post.urls')),
    url(r'^contact/', Contacts.as_view(), name='contacts'),
    url(r'^reservation-form/', ReservationForm.as_view(), name='reservation-form'),
    url(r'^reservation/', Reservation.as_view(), name='reservation'),
    url(r'^googlee0c974bb20845588\.html$', lambda r: HttpResponse("google-site-verification: googlee0c974bb20845588.html")),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},name='django.contrib.sitemaps.views.sitemap'),
    url(r'^robots\.txt', include('robots.urls')),
    url(r'^rss/',ServicesFeed(), name='feeds'),
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns.append(url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))