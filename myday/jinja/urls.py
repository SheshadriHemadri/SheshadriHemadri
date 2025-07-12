from django.urls import path
from . import views

urlpatterns = [
    path('', views.displaygreen, name='displaygreen'),
    ##path('product/<int:pk>/', views.product_detail, name='product_detail'),
]
