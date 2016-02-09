import os
from django.core.urlresolvers import reverse
from django.db import models
from model_utils.models import TimeStampedModel
from BS.services.models import TypeOfService


class Album(TimeStampedModel):
    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'
        db_table = 'album'

    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    tos = models.ForeignKey(TypeOfService, default='', verbose_name='Альбом услуги')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='Ссылка')

    def image(self):
        return self.tos.image_tag()

    def get_absolute_url(self):
        return reverse('album', kwargs={"slug": self.slug})

    def __str__(self):
        return self.tos.name

    image.short_description = 'Изображение'
    image.allow_tags = True


class Photo(TimeStampedModel):
    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографии'
        db_table = 'photos'

    album = models.ForeignKey(Album, verbose_name='Альбом')
    file = models.ImageField(upload_to='photos', verbose_name='Файл')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')

    def size(self):
        return "%.2fКб" % (self.file.size/1024)

    def file_name(self):
        return os.path.basename(self.file.name)

    def image_tag(self):
        if self.file:
            return u'<img src="%s" style="width:100px" />' % self.file.url
        else:
            return '(нет изображения)'

    def resolution(self):
        return '%sx%s' % (self.file.width,self.file.height)

    def __str__(self):
        return self.file.name

    size.short_description = 'Размер'
    file_name.short_description = 'Имя файла'
    resolution.short_description = 'Разрешение'
    image_tag.short_description = 'Изображение'
    image_tag.allow_tags = True