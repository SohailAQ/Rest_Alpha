from django.urls import path
from .views import TodoList, TodoDetail

urlpatterns = [
    path('todo/<int:pk>/', TodoDetail.as_view()),
    path('todo/', TodoList.as_view()),
]
