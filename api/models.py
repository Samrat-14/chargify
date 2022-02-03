from django.db import models

# Create your models here.

class Gps(models.Model):
    latitude = models.DecimalField(max_digits=8, decimal_places=5)
    longitude = models.DecimalField(max_digits=8, decimal_places=5)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.latitude)+","+str(self.longitude)

    class Meta:
        ordering = ['-timestamp']