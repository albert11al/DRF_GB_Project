from rest_framework import viewsets, mixins
from rest_framework.generics import get_object_or_404
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from .models import MyUser
from .serializers import UserModelSerializer
from rest_framework.permissions import DjangoModelPermissions

# просмотра списка и каждого пользователя в отдельности (id пользователей 6, 7 и 8)
# можно вносить изменения, нельзя удалять и создавать
class UserModelViewSet(
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet
):
    queryset = MyUser.objects.all()
    serializer_class = UserModelSerializer
    permission_classes = [DjangoModelPermissions]








