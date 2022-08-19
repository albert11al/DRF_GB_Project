from rest_framework import mixins
from rest_framework.pagination import LimitOffsetPagination
from TODO.models import Project, Todo
from TODO.serializers import ProjectSerializer, TodoSerializer
from rest_framework.viewsets import GenericViewSet, ModelViewSet

# для постраничного вывода установить размер страницы 10 записей;
class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10
#доступны все варианты запросов;
class ProjectViews(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = ProjectLimitOffsetPagination
    def get_queryset(self):
        return Project.objects.filter(name_todo='проект')

class TodoViews(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer




