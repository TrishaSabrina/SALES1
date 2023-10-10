from rest_framework import serializers
from .models import Sales

class SalesSerializers(serializers.ModelSerializer) :
    class Meta :
        model = Sales
        fields = "__all__"