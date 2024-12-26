from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GameViewSet, CardViewSet, UserViewSet, TeamViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'games', GameViewSet)
router.register(r'cards', CardViewSet)

urlpatterns = [
    path('', include(router.urls)),
]