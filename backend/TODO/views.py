from rest_framework import mixins
from rest_framework.pagination import LimitOffsetPagination
from TODO.models import Project, Todo
from TODO.serializers import ProjectSerializer, TodoSerializer
from rest_framework.viewsets import GenericViewSet

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
        return Project.objects.filter(name_todo__contains='проект')
class TodoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20
class TodoViews(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    pagination_class = TodoLimitOffsetPagination
    #добавить фильтрацию по проекту
    filterset_fields = ['project']
# при удалении не удалять Todo а выставлять признак, что оно закрыто
    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()






