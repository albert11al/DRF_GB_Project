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

        if first_name:
            params['first_name__contains'] = first_name
        if last_name:
            params['last_name__contains'] = last_name
        return MyUser.objects.filter(**params)

class UserCreateMutation(graphene.Mutation):
    class Arguments:
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        birthday_year = graphene.Int(required=True)
        email = graphene.String(required=True)
        is_superuser = graphene.Boolean(required=True)
        is_staff = graphene.Boolean(required=True)

    user = graphene.Field(UserObjectType)

    @classmethod
    def mutate(cls, root, info, first_name, last_name, birthday_year, email, is_superuser, is_staff):
        user = MyUser(
            first_name=first_name,
            last_name=last_name,
            birthday_year=birthday_year,
            email=email,
            is_superuser=is_superuser,
            is_staff=is_staff
        )
        user.save()
        return cls(user)

class UserUpdateMutation(graphene.Mutation):
    class Arguments:
        pk = graphene.Int(required=True)
        first_name = graphene.String(required=False)
        last_name = graphene.String(required=False)
        birthday_year = graphene.Int(required=False)
        email = graphene.String(required=False)
        is_superuser = graphene.Boolean(required=False)
        is_staff = graphene.Boolean(required=False)

    user = graphene.Field(UserObjectType)

    @classmethod
    def mutate(cls, root, info, pk, first_name=None, last_name=None, birthday_year=None, email=None, is_superuser=None, is_staff=None):
        user = MyUser.objects.get(pk=pk)

        if first_name:
            user.first_name = first_name

        if last_name:
            user.last_name = last_name

        if birthday_year:
            user.birthday_year = birthday_year

        if email:
            user.email = email

        if is_superuser:
            user.is_superuser = is_superuser

        if is_staff:
            user.is_staff = is_staff

        if first_name or last_name or birthday_year or email or is_superuser or is_staff:
            user.save()
        return cls(user)

class UserDeleteMutation(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        pk = graphene.ID()

    user = graphene.Field(UserObjectType)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        ok = False
        user = MyUser.objects.get(pk=kwargs["pk"])

        if user:
            ok = True
            user.delete()

        return UserDeleteMutation(ok=ok)

class Mutations(graphene.ObjectType):
    create_user = UserCreateMutation.Field()
    update_user = UserUpdateMutation.Field()
    delete_user = UserDeleteMutation.Field()

schema = graphene.Schema(query=Query, mutation=Mutations)
