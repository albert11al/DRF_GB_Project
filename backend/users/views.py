from rest_framework.viewsets import ModelViewSet
from .models import MyUser
from .serializers import UserModelSerializer
class UserModelViewSet(ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = UserModelSerializer
