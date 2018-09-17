from django.urls import path
from django.views.decorators.cache import cache_page
from app import views

cached_home = cache_page(60)(views.Home.as_view())

urlpatterns = [
    path('', cached_home, name='home'),
    path('book/', views.BookList.as_view(), name='book-list'),
    path('book/create/', views.BookCreate.as_view(), name='book-create'),
    path('book/<pk>/', views.BookDetail.as_view(), name='book-detail'),
    path('book/<pk>/update/', views.BookUpdate.as_view(), name='book-update'),
    path('author/', views.AuthorList.as_view(), name='author-list'),
    path('author/create/', views.AuthorCreate.as_view(), name='author-create'),
    path('author/<pk>/', views.AuthorDetail.as_view(), name='author-detail'),
    path('author/<pk>/update/', views.AuthorUpdate.as_view(), name='author-update'),
]
