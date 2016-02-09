#from ckeditor.fields import RichTextField
from django.db import models
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from taggit.managers import TaggableManager
from taggit.models import Tag, TaggedItem
from django.template.defaultfilters import slugify
from unidecode import unidecode

from djorm_pgfulltext.models import SearchManager
from djorm_pgfulltext.fields import VectorField

from ckeditor_uploader.fields import RichTextUploadingField



class RuTag(Tag):
    class Meta:
        proxy = True

    def slugify(self, tag, i=None):
        return slugify(unidecode(self.name))[:128]


class RuTaggedItem(TaggedItem):
     class Meta:
         proxy = True

     @classmethod
     def tag_model(cls):
         return RuTag


class Category(models.Model):
    class Meta:
        verbose_name='Категория статей'
        verbose_name_plural='Категории статей'
        db_table = 'category'

    name = models.CharField(max_length=200, verbose_name='Наименование')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='Ссылка')

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.name


class Post(models.Model):
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-created']
        db_table = 'article'

    title = models.CharField(max_length=200, verbose_name='Заголовок')
    body = RichTextUploadingField(verbose_name='Статья', config_name='default')#models.TextField(verbose_name='Статья')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='Ссылка')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    image = models.ImageField(upload_to='post',blank=True, default='post/default.jpg')
    pageviews = models.PositiveIntegerField(verbose_name='Количество просмотров', default=0, blank=True)
    tags = TaggableManager(through=RuTaggedItem) #through=RuTaggedItem
    category = models.ForeignKey(Category, default='', verbose_name='Категория')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')

    search_index = VectorField()
    objects = SearchManager(
        fields = ('title', 'description'),
        config = 'pg_catalog.russian',
        search_field = 'search_index',
        auto_update_search_field = True
    )

    def __str__(self):
        return self.title

    def get_object(self):
        return get_object_or_404(Post, slug__iexact=self.kwargs['slug'])

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"slug": self.slug})

    def image_tag(self):
        if self.image:
            return u'<img src="%s" style="width:100px" />' % self.image.url
        else:
            return '(нет изображения)'
    image_tag.short_description = 'Изображение'
    image_tag.allow_tags = True

