from rest_framework import serializers
from .models import User, Company, Products

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['company','ruc','web','user']

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['product','sku','price','discount','company']
    