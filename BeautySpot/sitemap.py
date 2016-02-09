from django.contrib.sitemaps import Sitemap

from BS.gallery.models import Album,Photo
from BS.post.models import Category,Post
from BS.services.models import Service

class PostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5
    protocol = 'http'

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.created

    def location(self, post):
        return "/post/" + post.slug

class CategorySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.2

    def items(self):
        return Category.objects.all()

    def location(self, obj):
        return "/category/" + obj.slug

class ServiceSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Service.objects.all()

    def location(self, obj):
        return '/services/'

class AlbumsSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Album.objects.all()

    def location(self, obj):
        return '/gallery/'+obj.slug

class HomeSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return ['index']

    def location(self, obj):
        return '/'