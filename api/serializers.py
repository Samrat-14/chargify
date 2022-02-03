from rest_framework.serializers import ModelSerializer
from .models import Gps


class GpsSerializer(ModelSerializer):
    class Meta:
        model = Gps
        fields = '__all__'