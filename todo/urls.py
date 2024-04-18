from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('completed', views.completed, name='done'),
    path('remaining', views.remaining, name='remaining'),
    path('add', views.add_todo, name='add_todo'),
    path('request_to_delete/<int:todo_id>/', views.request_to_delete_todo, name='request_to_delete_todo'),
    path('delete/<int:todo_id>/', views.delete_todo, name='delete_todo'),
    path('detail/<int:todo_id>/', views.todo_detail, name='detail'),
    path('toggle/<int:todo_id>/', views.toggle_todo, name='toggle'),
]
