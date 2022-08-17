# Generated by Django 3.2.14 on 2022-08-14 07:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name_todo', models.CharField(max_length=64)),
                ('link_repository', models.URLField(max_length=128)),
                ('users_work', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Staff')),
            ],
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_todo', models.TextField(help_text='Опишите суть задачи.')),
                ('creating', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updating', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('is_active', models.BooleanField(default=True, verbose_name='TODO is active')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TODO.project')),
                ('user_note', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
