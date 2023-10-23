from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product  # Specifies the model to be serialized (Product)
        fields = "__all__"  # Includes all fields from the model in the serialization
