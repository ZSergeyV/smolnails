from decimal import Decimal
from django.db import models
from django.core.urlresolvers import reverse


class TypeOfService(models.Model):
    class Meta:
        verbose_name = 'Категория услуг'
        verbose_name_plural = 'Категории услуг'
        db_table = 'type_of_service'

    name = models.CharField(max_length=200, verbose_name='Наименование')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='Ссылка')
    image = models.ImageField(upload_to='services', verbose_name='Изображение', blank=True, default='services/default.jpg')
    descriptions = models.TextField(verbose_name='Описание', blank=True)

    def get_absolute_url(self):
        return reverse('services', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name

    def image_tag(self):
        if self.image:
            return u'<img src="%s" style="width:100px" />' % self.image.url
        else:
            return '(нет изображения)'
    image_tag.short_description = 'Изображение'
    image_tag.allow_tags = True


class Service(models.Model):
    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        db_table = 'service'

    name = models.CharField(max_length=200, verbose_name='Наименование')
    body = models.TextField (verbose_name='Описание услуги')
    new_price = models.DecimalField(max_digits=6, decimal_places=2, default=Decimal(0.00), verbose_name='Новая цена')
    old_price = models.DecimalField(max_digits=6, decimal_places=2, default=Decimal(0.00), verbose_name='Старая цена')
    type_of_service = models.ForeignKey(TypeOfService, default='', verbose_name='Вид услуг')

    def __str__(self):
        return self.name


class AdditionalInformation(models.Model):
    class Meta:
        verbose_name = 'Дополнительная информация'
        verbose_name_plural = 'Дополнительная информация'
        db_table = 'additional_information'

    title = models.CharField(max_length=200, verbose_name='Наименование',blank=True)
    descriptions = models.TextField(verbose_name='Описание', blank=True)
    price = models.DecimalField(verbose_name='Цена', max_digits=6, decimal_places=2, default=Decimal(0.00))
    service = models.ForeignKey(Service, default='', verbose_name='Услуга')
