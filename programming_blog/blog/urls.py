from django.urls import path
from .views import BlogHomeimport *

urlpatterns = [
    path('', BlogHome.as_vies(), name='index'),
]