import csv
from django.core.management.base import BaseCommand
from django_netology.models import Phone
from django.utils.text import slugify


class Command(BaseCommand):
    help = 'Import phone data from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        csv_file = options['csv_file']

        with open(csv_file, 'r') as file:
            reader = csv.reader(file, delimiter=';')
            next(reader)  # Пропуск заголовков
            for row in reader:
                id = row[0]
                name = row[1]
                image = row[2]
                price = row[3]
                release_date = row[4]
                lte_exists = row[5]
                slug = slugify(name)

                phone, created = Phone.objects.get_or_create(id=id,
                                                             defaults={'name': name, 'price': price, 'image': image,
                                                                       'release_date': release_date,
                                                                       'lte_exists': lte_exists, 'slug': slug})