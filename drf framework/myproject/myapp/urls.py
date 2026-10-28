from django.urls import path
from .views import Todo_list,todo_detail

urlpatterns = [
    path('todos',Todo_list),
    path('todos/<int:id>',todo_detail),


]