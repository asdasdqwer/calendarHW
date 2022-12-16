from django.urls import path

from .views import pomodoroPage

urlpatterns = [
    path('', pomodoroPage)
]
