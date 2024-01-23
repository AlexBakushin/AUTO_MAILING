from django.urls import path
from blog.apps import BlogConfig
from django.views.decorators.cache import cache_page
from blog.views import BlogCreateView, BlogListView, BlogDetailView, BlogUpdateView, BlogDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('create/', cache_page(5 * 60)(BlogCreateView.as_view()), name='create'),
    path('', cache_page(5 * 60)(BlogListView.as_view()), name='list'),
    path('view/<int:pk>/', cache_page(5 * 60)(BlogDetailView.as_view()), name='view'),
    path('edit/<int:pk>/', cache_page(5 * 60)(BlogUpdateView.as_view()), name='edit'),
    path('delete/<int:pk>/', cache_page(5 * 60)(BlogDeleteView.as_view()), name='delete'),
]
