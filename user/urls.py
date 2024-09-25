from django.urls import path
from . import views





urlpatterns = [
    path('create_user/', views.create_user, name='Create_User'),
    path('user/', views.show_user, name='ShowUser'),
    path('delete-user/<int:user_id>/', views.delete_user, name='delete_user')


]
