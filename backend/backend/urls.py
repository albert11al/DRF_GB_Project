from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import UserModelViewSet
from TODO.views import ProjectViews, TodoViews
from rest_framework.authtoken import views
from users.views import *

#router = DefaultRouter()
#router.register('users', UserModelViewSet)
#router.register('projects', ProjectViews)
#router.register('todos', TodoViews)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('users.urls')),
    path('api-token-auth/', views.obtain_auth_token),
    #path('api/<str:version>/users', UserModelViewSet.as_view({'get': 'list'})),
    path('api/2.0/', include('users.urls', namespace='2.0')),

]
