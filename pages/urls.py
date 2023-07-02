from rest_framework.routers import DefaultRouter
from django.urls import path, include

from pages.views import PageViewSet

router = DefaultRouter()

router.register('pages', PageViewSet)

urlpatterns =[
    path('', include(router.urls))
]