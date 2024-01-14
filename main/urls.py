from django.urls import path
from main.apps import MainConfig
from main.views import index


app_name = MainConfig.name

urlpatterns = [
    path('', index, name='index'),
    # path('contacts/', contacts, name='contacts'),
    # path('product/<slug:slug>/', ProductDetailView.as_view(), name='product'),
    # path('create/', ProductCreateView.as_view(), name='create_product'),
    # path('edit/<slug:slug>/', ProductUpdateView.as_view(), name='update_product'),
    # path('delete/<slug:slug>/', ProductDeleteView.as_view(), name='delete_product')
]
