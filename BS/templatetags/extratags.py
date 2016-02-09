from django import template
from taggit.models import Tag
from BS.gallery.models import Photo, Album
from BS.post.models import Category, Post
from BS.services.models import TypeOfService, AdditionalInformation


register = template.Library()

@register.inclusion_tag('templatetags/slider.html')
def slider_tag():
    pass


@register.inclusion_tag('templatetags/footer.html')
def footer_tag():
    pass


@register.inclusion_tag('templatetags/services.html')
def services_tag():
    return {'type_services':TypeOfService.objects.all()}


@register.inclusion_tag('templatetags/additional_information.html')
def addit_inf(servic_id):
    return {'add_inf':AdditionalInformation.objects.filter(service__id=servic_id)}


@register.inclusion_tag('templatetags/gallery.html')
def gallery_tag():
    return {'photo':Photo.objects.order_by('-created')[:8]}


@register.inclusion_tag('templatetags/blog.html')
def blog_tag():
    return {'post':Post.objects.order_by('-pageviews')[:4]}

@register.inclusion_tag('templatetags/testimonials.html')
def testimonials_tag():
    pass


@register.inclusion_tag('templatetags/brands.html')
def brands_tag():
    pass


@register.inclusion_tag('templatetags/side_find.html')
def side_find():
    pass

@register.inclusion_tag('templatetags/side_category.html')
def side_category():
    return {'category':Category.objects.all()}


@register.inclusion_tag('templatetags/side_popular_post.html')
def side_popular_post():
    return {'post':Post.objects.order_by('-pageviews')[:3]}


@register.inclusion_tag('templatetags/side_tags.html')
def side_tags():
    return {'tags':Tag.objects.all()}


@register.inclusion_tag('templatetags/related_post.html')
def related_post(category,post_exclude):
    return {'posts':Post.objects.filter(category__id=category).exclude(id=post_exclude)[:3]}


@register.simple_tag(name='keywords')
def keyworsd(album_id = None):
    if album_id == None:
        object = list(Photo.objects.all().values_list('description',flat=True))
    else:
        object = list(Photo.objects.filter(album__id=album_id).values_list('description',flat=True))
    tmp=[x for x in object if x]
    return ','.join(tmp)