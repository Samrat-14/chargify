from django.db import models
import uuid

# Create your models here.

class Gps(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    latitude = models.DecimalField(max_digits=8, decimal_places=5)
    longitude = models.DecimalField(max_digits=8, decimal_places=5)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.latitude)+","+str(self.longitude)

    class Meta:
        ordering = ['-timestamp']