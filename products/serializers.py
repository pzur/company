from rest_framework import serializers
from .models import Company, Products
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email']

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['company','ruc','web','user']

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['product','sku','price','discount','company']
    