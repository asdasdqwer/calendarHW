from django.urls import path
from .views import editTask

urlpatterns = [
    path('<int:id>/', editTask, name="edit")
]