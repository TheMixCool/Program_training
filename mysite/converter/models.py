from django.db import models

class MyClass(models.Model):
    request = models.CharField(max_length=256, null=True)
