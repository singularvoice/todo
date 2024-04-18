from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('completed', views.completed, name='done'),
    path('remaining', views.remaining, name='remaining'),
    path('add', views.add_todo, name='add_todo'),
    path('delete', views.delete_todo, name='delete_todo'),
    path('detail', views.todo_detail, name='detail'),
    # path('', views.todo_list, name='todo_list'),
    # path('add/', views.add_todo, name='add_todo'),
    # path('delete/<int:todo_id>/', views.delete_todo, name='delete_todo'),
    # path('toggle/<int:todo_id>/', views.toggle_todo, name='toggle_todo'),
]
