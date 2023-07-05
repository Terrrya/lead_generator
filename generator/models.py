from django.db import models


class Lead(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, null=True)
    site_url = models.URLField(null=True)
    location = models.CharField(max_length=255)
    rating = models.FloatField(null=True)
