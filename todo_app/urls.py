from django.contrib import admin
from django.urls import path

from . import views

app_name = 'todo_app'

urlpatterns = [
   path('', views.index, name='index'),
   path('change_status', views.change_status, name='change_status'),
   path('completed_todos/', views.completed_todos, name='completed_todos'),
   path('delete_todo/', views.delete_todo, name='delete_todo'),
   path('todo_details/', views.todo_details, name='todo_details'),
   path('pdf_download/', views.pdf_download, name='pdf_download'),

   # path('show_todo/<str:pk>', views.show_todo_pk, name='show_todo_pk'),
]