from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('devices/', Devices.as_view()),
    path('devices/<str:pk>', Device.as_view()),
    path('resetPins/<str:pk>', ResetPin.as_view()),
    path('resetPins/', ResetPin.as_view())
]
