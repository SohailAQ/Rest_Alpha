from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Todo
from .serializers import TodoSerializer


class TodoList(ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoDetail(RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
