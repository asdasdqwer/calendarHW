from django.urls import path

from .views import calendarRender

urlpatterns = [
    path('', calendarRender)
]
