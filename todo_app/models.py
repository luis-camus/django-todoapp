from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Todo(models.Model):
    name = models.CharField(max_length=100)
    priority = models.BooleanField(default=False)
    done = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name