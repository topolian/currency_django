from django.db import models


class Rate(models.Model):
    sale = models.DecimalField(max_digits=5, decimal_places=2)
    buy = models.DecimalField(max_digits=5, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    source = models.CharField(max_length=32)
    type = models.CharField(max_length=3)   # noqa


class ContactUs(models.Model):
    email_from = models.EmailField(max_length=70)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=700)


class Source(models.Model):
    source_url = models.URLField(max_length=255)
    name = models.CharField(max_length=64)

