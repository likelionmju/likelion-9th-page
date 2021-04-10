from django.urls import path
from . import views

urlpatterns = [
    path('', views.assignment, name="assignment"),
    path('create', views.create, name="create"),
    path('detail', views.detail, name="detail"),
]