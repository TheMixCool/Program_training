from django.db import models

class MyClass(models.Model):
    request = models.CharField(max_length=256, null=True)
    speed = models.DecimalField(max_digits=100, decimal_places=3, null = True)
