from rest_framework import serializers
from .models import Stu

class StuSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Stu
        fields = ('roll_no','name','address')
        #fields=' __all__'
