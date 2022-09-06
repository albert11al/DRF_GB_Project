from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate
from .views import UserModelViewSet
from .models import MyUser
class UserTestCase(TestCase):
    def setUp(self) -> None:
        self.user = MyUser.objects.create_superuser(username='aaaaa@a.com', password='master')
        self.author = MyUser.objects.create(first_name="lacaz", last_name="jenderman", birthday_year=2002, email="drfAdmin1@drf.com")
    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/users/')
        view = UserModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    def test_create_admin(self):
        factory = APIRequestFactory()
        request = factory.get('/api/users/')
        force_authenticate(request, user=self.user)
        view = UserModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)


