from django.urls import path
from . import views
from .models import Menu

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    # Add the remaining URL path configurations here
    path('menu/', views.Menu.as_view(), name="menu"),
    path('menu/<int:pk>/', views.MenuIem.as_view(model=Menu), name="menu_item")
]
