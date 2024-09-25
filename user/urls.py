from django.urls import path
from . import views





urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('create/', views.create_user, name='create_user'),
    path('delete/', views.delete_user, name='delete_user'),
    path('show/', views.show_user, name='show_user'),
    path('next_step/', views.next_step, name='next_step')


]
