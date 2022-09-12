from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from users.views import UserModelViewSet
from TODO.views import ProjectViews, TodoViews
from rest_framework.authtoken import views
from drf_yasg.views import get_schema_view
from drf_yasg.openapi import Info, License, Contact
from graphene_django.views import GraphQLView


schema_view = get_schema_view(
    Info(
        title='TODO',
        default_version='1.0',
        description='description',
        license=License(name='MIT'),
        contact=Contact(email='test@yandex.ru')
    )
)


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
    path('swagger', schema_view.with_ui()),
    re_path(r'swagger(?P<format>\.json|\.yaml)', schema_view.without_ui()),
    path("graphql/", GraphQLView.as_view(graphiql=True)),

]
