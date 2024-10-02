from django.urls import path, include
from rest_framework import routers
from cats.views import CatsViewSet


router = routers.DefaultRouter()

router.register(r'cats', CatsViewSet, basename='кошка')


urlpatterns = [
    path('', include(router.urls)),
]
