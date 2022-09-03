import uuid
from django.db import models
from users.models import MyUser

class Project(models.Model):

    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name_todo = models.CharField(max_length=64)
    link_repository = models.URLField(max_length=128)
    users_work = models.ManyToManyField(MyUser, verbose_name='Staff')

class Todo(models.Model):

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    text_todo = models.TextField(help_text='Опишите суть задачи.')
    creating = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updating = models.DateTimeField(auto_now=True, verbose_name='Updated at')
    user_note = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True, verbose_name='TODO is active')

