from datetime import datetime
import csv
from yourapp.models import Phone
from django.utils.text import slugify
from django.shortcuts import render


def importdatafromcsv(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        csvdata = csv.DictReader(file, delimiter=';')
        for row in csvdata:
            phone = Phone(
                id=row['id'],
                name=row['name'],
                image=row['image'],
                price=row['price'],
                releasedate=datetime.strptime(row['releasedate'], '%Y-%m-%d').date(),
                lteexists=row['lteexists'] == 'True',
                slug=slugify(row['name'])
            )
            phone.save()


def getsortedphones(request):
    sortparam = request.GET.get('sort', '')
    if sortparam == 'name':
        phones = Phone.objects.all().order_by('name')
    elif sortparam == 'minprice':
        phones = Phone.objects.all().order_by('price')
    else:
        phones = Phone.objects.all()

    return render(request, 'phones_list.html', {'phones': phones})
