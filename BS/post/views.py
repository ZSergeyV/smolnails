from django.db.models import F
from django.views import generic
from taggit.models import Tag
from .models import Post, Category
from meta.views import MetadataMixin

class SearchContent(generic.ListView):
    template_name = 'search-results.html'
    model = Post
    paginate_by = 5

    def get_queryset(self):
        search_text=''
        tmp=self.request.GET['search']
        if tmp :
            search_text=tmp.split(' ')
            search_text = '|'.join(search_text)

        return Post.objects.search(search_text)

    def get_context_data(self, **kwargs):
        context = super(SearchContent,self).get_context_data(**kwargs)
        context['search_text'] = self.request.GET['search']
        return context


class PostList(generic.ListView):
    template_name = 'blog.html'
    model = Post
    paginate_by = 4


class PostDetail(MetadataMixin, generic.DetailView):
    model = Post
    template_name = 'post.html'

    MetadataMixin.use_og = True

    def get_meta_keywords(self, context):
        return [', '.join(list(self.object.tags.all().values_list('name', flat=True)))]

    def get_meta_title(self, context):
        return self.object.title

    def get_meta_description(self, context):
        return self.object.description

    def get_meta_image(self, context):
        return self.object.image.url

    def get_meta_url(self, context={}):
        return self.request.path

    def get_context_data(self, **kwargs):
        context = super(PostDetail,self).get_context_data(**kwargs)
        Post.objects.filter(pk=self.object.pk).update(pageviews=F("pageviews") + 1)
        return context


class CategoryDetail(generic.DetailView):
    model = Category
    template_name = 'category.html'


class TagsList(generic.ListView):
    template_name = 'tags.html'
    model = Post
    paginate_by = 4

    def get_queryset(self):
        qs = Post.objects.filter(tags__slug=self.kwargs['slug']).order_by('-created')
        return qs

    def get_context_data(self, **kwargs):
        context = super(TagsList, self).get_context_data(**kwargs)
        name_tag = Tag.objects.filter(slug=self.kwargs['slug']).values_list('name')
        context['name_tag'] = name_tag[0][0]
        return context
