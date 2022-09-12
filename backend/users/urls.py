from django.urls import path,  include
from rest_framework.routers import DefaultRouter
from .views import UserModelViewSet
from TODO.views import ProjectViews, TodoViews

app_name = 'users'

router = DefaultRouter()
router.register("users", UserModelViewSet)
router.register("projects", ProjectViews)
router.register("todos", TodoViews)

urlpatterns = [
    path('', include(router.urls))
]