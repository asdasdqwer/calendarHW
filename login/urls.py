from django.urls import path

from .views import loginInterface

urlpatterns = [
    path('', loginInterface)
]
