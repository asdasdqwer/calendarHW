from django.urls import path

from .views import rickroll

urlpatterns = [
    path('', rickroll)
]
