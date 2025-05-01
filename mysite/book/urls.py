from rest_framework import routers
from .views import *
from django.urls import path, include

router = routers.SimpleRouter()

router.register(r'users', UserProfileViewSet, basename='users')
router.register(r'event', EventViewSet, basename='event')
router.register(r'booking', BookingViewSet, basename='booking')


urlpatterns = [
    path('', include(router.urls)),
]