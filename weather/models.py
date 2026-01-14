from django.db import models

# Create your models here.
class SearchHistory(models.Model):
    city_name = models.CharField(max_length=100)
    temperature = models.FloatField(null=True, blank=True)
    humidity = models.IntegerField(null=True, blank=True)
    pressure = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
