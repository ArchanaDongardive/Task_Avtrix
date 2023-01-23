from app1.models import Product
from rest_framework import serializers


class ProductSerailizer(serializers.Serializer):
    Order_date = serializers.DateField()
    Region = serializers.CharField(max_length=200)
    City = serializers.CharField(max_length=200)
    Category = serializers.CharField(max_length=200)
    Product = serializers.CharField(max_length=200)
    Quantity = serializers.IntegerField()
    UnitPrice = serializers.FloatField()


    def create(self,validated_data):
        prod = Product.objects.create(**validated_data)
        return prod 

    def update(self, instance, validated_data):  # python dict
        instance.Order_date = validated_data.get('Order_date', instance.Order_date)
        instance.Region = validated_data.get('Region', instance.Region)
        instance.City = validated_data.get('City', instance.City)  # None
        instance.Category = validated_data.get('Category', instance.Category) # None
        instance.Product = validated_data.get('Product', instance.Product)
        instance.Quantity = validated_data.get('Quantity', instance.Quantity)
        instance.UnitPrice = validated_data.get('UnitPrice', instance.UnitPrice)
        instance.save()
        return instance    


       
