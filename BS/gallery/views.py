from django.views import generic
from .models import Album


class Gallery(generic.ListView):
    model = Album
    template_name = "gallery.html"


class AlbumView(generic.DetailView):
    model = Album
    template_name = 'photos.html'
