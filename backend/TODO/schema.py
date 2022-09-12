import graphene
from users.models import MyUser
from .models import Project, Todo
from graphene_django import DjangoObjectType

class UserObjectType(DjangoObjectType):
    class Meta:
        model = MyUser
        field = "__all__"

class ProjectObjectType(DjangoObjectType):
    class Meta:
        model = Project
        field = "__all__"

class TodoObjectType(DjangoObjectType):
    class Meta:
        model = Todo
        field = "__all__"

class Query(graphene.ObjectType):

    all_users = graphene.List(UserObjectType)

    def resolve_all_users(self, info):
        return MyUser.objects.all()

    all_projects = graphene.List(ProjectObjectType)

    def resolve_all_projects(self, info):
        return Project.objects.all()

    all_todos = graphene.List(TodoObjectType)

    def resolve_all_todos(self, info):
        return Todo.objects.all()

    get_user_by_id = graphene.Field(UserObjectType, pk=graphene.Int(required=True))

    def resolve_get_user_by_id(self, info, pk):
        # return MyUser.objects.get(pk=1).todo_set.all()
        return MyUser.objects.get(pk=pk)

    get_user_by_name = graphene.List(
        UserObjectType,
        first_name=graphene.String(required=False),
        last_name=graphene.String(required=False)
    )

    def resolve_get_user_by_name(self, info, first_name=None, last_name=None):
        params = {}
        if not first_name and not last_name:
            return MyUser.objects.all()
        if first_name :
            params['first_name'] = first_name
        if last_name :
            params['last_name'] = last_name
        return MyUser.objects.filter(**params)

schema = graphene.Schema(query=Query)
