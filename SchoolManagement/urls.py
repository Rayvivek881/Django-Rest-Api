from django.urls import path, include
from .views import StudentViewSet, TeacherViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('student', StudentViewSet, basename='student')
router.register('teacher', TeacherViewSet, basename='teacher')

urlpatterns = [
  path('', include(router.urls)),
]
