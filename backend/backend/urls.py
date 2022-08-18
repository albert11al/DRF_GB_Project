from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users import views
from users.views import UserModelViewSet
from TODO.views import ProjectViews, TodoViews

router = DefaultRouter()
router.register('users', UserModelViewSet)
router.register('project', ProjectViews)
router.register('todo', TodoViews)
router.register('base', views.UserViewSet, basename='user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls)),
    path('viewsets/', include(router.urls)),

]
