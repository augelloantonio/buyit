from rest_framework import serializers


class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=120)
    price = serializers.CharField()

class MonthlyEarning(serializers.Serializer):
    total = serializers.CharField()
    date = serializers.DateField()