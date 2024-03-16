
from django.urls import path
from .views import catalog

urlpatterns = [
    path('catalog/', catalog, name='catalog'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('catalog/iphone-x/<slug>/', views.iphonexinfo, name='iphonexinfo'),
]