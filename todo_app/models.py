from django.db import models

# Create your models here.
class todo(models.Model):
    name = models.CharField(max_length=100)
    priority = models.BooleanField(default=False)
    done = models.BooleanField(default=False)