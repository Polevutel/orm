from django.shortcuts import render
from django_netology.models import Phone

def catalog(request):
    phones = Phone.objects.all()
    return render(request, 'catalog.html', {'phones': phones})

from .models import Phone

def iphonexinfo(request, slug):
    phone = Phone.objects.get(slug=slug)
    return render(request, 'iphonexinfo.html', {'phone': phone})