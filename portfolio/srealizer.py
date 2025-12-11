from rest_framework import serializers
from .models import entry

class SS(serializers.ModelSerializer):
     class Meta:
        model = entry
        fields = '__all__'

