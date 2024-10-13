from rest_framework import serializers
from .models import Product


class GetOneProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    discount = serializers.IntegerField()
    price_cap = serializers.IntegerField()

    class Meta:
        model = Product
        fields = ["name", "result", "user", 'created', 'updated']  # Include other fields as needed
        extra_kwargs = {
            "result": {"required": False},  # Not required
            "user": {
                "required": False
            },  # Not required (assumed this will be set later)
        }
