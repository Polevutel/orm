from django.db import models

class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    image = models.URLField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    releasedate = models.DateField()
    lteexists = models.BooleanField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
