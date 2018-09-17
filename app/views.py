from django import views
from django.views.decorators.cache import cache_page
from app import models


class Home(views.generic.TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book'] = models.Book.of_the_day.get()
        return context


class BookList(views.generic.ListView):
    queryset = models.Book.objects.all().prefetch_related('authors')
    template_name = 'book/list.html'
    context_object_name = 'books'
    paginate_by = 5


class BookDetail(views.generic.DetailView):
    model = models.Book
    template_name = 'book/detail.html'
    context_object_name = 'book'


class BookCreate(views.generic.CreateView):
    model = models.Book
    template_name = 'book/create.html'
    fields = ['title', 'authors', 'price', 'cover_image', 'description']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['authors'] = models.Author.objects.all()
        return context


class BookUpdate(views.generic.UpdateView):
    model = models.Book
    template_name = 'book/update.html'
    fields = ['title', 'authors', 'price', 'cover_image', 'description']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['authors'] = models.Author.objects.all()
        return context


class AuthorList(views.generic.ListView):
    model = models.Author
    template_name = 'author/list.html'
    context_object_name = 'authors'
    paginate_by = 5


class AuthorDetail(views.generic.DetailView):
    model = models.Author
    template_name = 'author/detail.html'
    context_object_name = 'author'


class AuthorCreate(views.generic.CreateView):
    model = models.Author
    template_name = 'author/create.html'
    fields = ['name']


class AuthorUpdate(views.generic.UpdateView):
    model = models.Author
    template_name = 'author/update.html'
    fields = ['name']
