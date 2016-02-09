from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Rss201rev2Feed
from django.contrib.sites.models import Site
from .models import Service


class ServiceFeedGenerator(Rss201rev2Feed):
    # def root_attributes(self):
    #         attrs = super(ServiceFeedGenerator, self).root_attributes()
    #         attrs['xmlns:itunes'] = 'http://www.itunes.com/dtds/podcast-1.0.dtd'
    #         return attrs

    def add_root_elements(self, handler):
        site = Site.objects.get_current().domain
        super(ServiceFeedGenerator, self).add_root_elements(handler)
        handler.startElement('image', {})
        handler.addQuickElement("url", 'http://127.0.0.1:8000/static/img/logo_rss.png')
        handler.addQuickElement("title", site)
        handler.addQuickElement("link", 'http://'+site)
        handler.endElement('image')
        # contents={ аттрибуты элемента
        #          'url': 'http://www.example.com/images/logo.jpg',
        #          'title': 'Some title',
        #          'link': 'http://www.example.com/',
        #      })

    def add_item_elements(self, handler, item):
        super(ServiceFeedGenerator, self).add_item_elements(handler, item)
        handler.addQuickElement('category', str(item['category']))

class ServicesFeed(Feed):
    title = "Услуги мастера ногтевого сервиса (smolnails.ru)"
    link = "/services/"
    #description_template = 'feeds/services.html'
    feed_type = ServiceFeedGenerator

    def items(self):
        return Service.objects.all()

    def item_link(self, item):
        return '/services/'

    def item_description(self, item):
        return item.body

    def item_guid(self,item):
        return str(item.id)

    def item_extra_kwargs(self, item):
        return { 'category': item.type_of_service.name}