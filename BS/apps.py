from django.apps import AppConfig

class GalleryConfig(AppConfig):
    name = 'BS.gallery'
    verbose_name = 'Галерея'


class ServicesConfig(AppConfig):
    name = 'BS.services'
    verbose_name = 'Услуги'


class PostConfig(AppConfig):
    name = 'BS.post'
    verbose_name = 'Статьи'

