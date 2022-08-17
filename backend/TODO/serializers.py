from rest_framework.renderers import JSONRenderer
from rest_framework.serializers import ModelSerializer
from TODO.models import Project, Todo

class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ['name_todo', 'link_repository', 'users_work']

class TodoSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'

