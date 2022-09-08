from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from users.models import MyUser
from .models import Project
from .models import Todo
from mixer.backend.django import mixer

class ProjectAPIClient(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.project = mixer.blend(Project)
        self.user = MyUser.objects.create_superuser(username='aaaaa@a.com', password='master')

    def test_get_detail(self):
        response = self.client.get(f'/api/projects/{self.project.uid}')
        self.assertEqual(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)

