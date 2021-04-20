from django.db import models

# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=120) # max_lenght = required
    description = models.TextField(blank=True, null=False)
    price       = models.DecimalField(decimal_places=2, max_digits=10000)
    active      = models.TextField()
    featured    = models.BooleanField(default=True)