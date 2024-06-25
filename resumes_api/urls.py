from django.urls import path, include
from .views import ResumeViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
router.register(r'resume', ResumeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
