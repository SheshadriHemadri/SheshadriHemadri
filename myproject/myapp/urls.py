# myapp/urls.py
from django.urls import path
from .views import StudentCreateView, StudentListView 
from .views import StudentUpdateView, StudentDeleteView
urlpatterns = [
    path('', StudentListView.as_view(), name='Student_list'),
    path('create/', StudentCreateView.as_view(), name='Student_create'),
    path('update/<int:pk>/', StudentUpdateView.as_view(), name='Student_update'),
    path('delete/<int:pk>/', StudentDeleteView.as_view(), name='Student_delete'),
]
