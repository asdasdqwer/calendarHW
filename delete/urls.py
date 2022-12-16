from django.urls import path

from .views import deleteTask

urlpatterns = [
    path('<int:id>', deleteTask)
]