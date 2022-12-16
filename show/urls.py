from django.urls import path

from .views import showTask

urlpatterns = [
    path('<int:id>', showTask)
]