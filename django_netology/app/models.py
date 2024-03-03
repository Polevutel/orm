from django.db import models

class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=100)
import csv
from datetime import datetime
from yourapp.models import Phone
from django.utils.text import slugify

def import_data_from_csv(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        csv_data = csv.DictReader(file, delimiter=';')
        for row in csv_data:
            phone = Phone(
                id=row['id'],
                name=row['name'],
                image=row['image'],
                price=row['price'],
                release_date=datetime.strptime(row['release_date'], '%Y-%m-%d').date(),
                lte_exists=row['lte_exists'] == 'True',
                slug=slugify(row['name'])
            )
            phone.save()
def get_sorted_phones(request):
    sort_param = request.GET.get('sort', '')
    if sort_param == 'name':
        phones = Phone.objects.all().order_by('name')
    elif sort_param == 'min_price':
        phones = Phone.objects.all().order_by('price')
    else:
        phones = Phone.objects.all()
    return phones
