from django.urls import path

from .views import logout_user

urlpatterns = [
    path('', logout_user)
]