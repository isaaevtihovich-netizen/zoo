from django.contrib import admin
from django.urls import path
from first import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('about/', views.about_view, name='about'),
    path('contacts/', views.contacts_view, name='contacts'),
    path('how_to_find/', views.how_to_find_view, name='how_to_find'),
    path('animals/', views.animals_view, name='animals'),
]