from django.urls import path

from .views import stufeView

urlpatterns = [
    path('', stufeView)
]
