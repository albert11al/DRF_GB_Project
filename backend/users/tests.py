from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APITestCase
from .views import UserModelViewSet
from .models import MyUser
from mixer.backend.django import mixer

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

class UserClientTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = MyUser.objects.create_superuser(username='aaaaa@a.com', password='master')
        self.author = MyUser.objects.create(first_name="lacaz", last_name="jenderman", birthday_year=2002,
                                            email="drfAdmin1@drf.com")

    def test_get_list(self):
        self.client.force_authenticate(self.user)
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_list_1(self):
        self.client.force_login(user=self.user)
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.client.logout()
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    #def test_post(self):
        #self.client.force_login(user=self.user)
        #response = self.client.post('/api/users/', {
            #"first_name": "konor",
            #"last_name": "makcgregar",
            #"birthday_year": 1992,
            #"email": "aaaaa@a.com"
        #})
        #self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        #author = MyUser.objects.get(pk=response.data.get('id'))
        #self.assertEqual(author.last_name, 'makcgregar')



