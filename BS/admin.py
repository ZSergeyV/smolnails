from django.contrib import admin

# Register your models here.
from BS.post.models import Category, Post
from BS.services.models import TypeOfService, Service, AdditionalInformation
from BS.gallery.models import Album, Photo


class TypeOFServicesAdmin(admin.ModelAdmin):
    list_display = ('name','image_tag',)
    prepopulated_fields = {"slug": ("name",)}


class AdditionalInformationInline(admin.StackedInline):
    model = AdditionalInformation
    extra = 1


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name','type_of_service',)
    inlines = [AdditionalInformationInline,]


class AlbumAdmin(admin.ModelAdmin):
      list_display = ('tos','description','image' )


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('file_name','description','resolution','size','image_tag',)



class CategoryAdmin(admin.ModelAdmin):
      list_display = ('name',)
      prepopulated_fields = {"slug": ("name",)}


class PostAdmin(admin.ModelAdmin):
      list_display = ("title", "created", 'image_tag')
      prepopulated_fields = {"slug": ("title",)}
      search_fields = ('title','body')



admin.site.register(TypeOfService, TypeOFServicesAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(AdditionalInformation)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
