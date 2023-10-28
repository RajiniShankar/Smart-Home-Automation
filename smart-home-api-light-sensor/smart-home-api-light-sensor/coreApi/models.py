from django.db import models

# Create your models here.
class Device(models.Model):
    id = models.CharField(unique=True, primary_key=True, max_length=3)
    name = models.CharField(max_length=2550)
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.id + ', ' + self.name + ', ' + str(self.status)
