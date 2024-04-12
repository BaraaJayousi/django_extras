from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('products', views.Products.as_view()),
    path('products/<int:id>', views.EditProduct.as_view(), name='edit_product'),
]
