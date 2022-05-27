from rest_framework import serializers
from ICS.models import DualDeskRequest

class DualDeskSerializer(serializers.ModelSerializer):
    class Meta():
        model = DualDeskRequest
        fields = '__all__'
