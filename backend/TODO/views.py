from TODO.models import Project, Todo
from TODO.serializers import ProjectSerializer, TodoSerializer
from rest_framework.viewsets import ModelViewSet

class ProjectViews(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class TodoViews(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer



