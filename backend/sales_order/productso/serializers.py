from rest_framework import serializers
from .models import Productso

class ProductsoSerializers(serializers.ModelSerializer) :
    class Meta :
        model = Productso
        fields = "__all__"