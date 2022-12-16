from django.urls import path

from .views import changeView

urlpatterns = [
    path('', changeView)
]
