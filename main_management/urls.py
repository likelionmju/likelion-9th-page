from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_management, name="main"),
    path('history/', views.main_management, name="history"),
    path('manager/', views.main_management, name="manager"),

]