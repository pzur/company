from rest_framework import generics
from django.contrib.auth.models import User
import json
from django.http import HttpResponse
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from .serializers import CompanySerializer, ProductsSerializer
from rest_framework.permissions import AllowAny
from .models import Company, Products

from rest_framework.authtoken.models import Token
from rest_framework import permissions
from rest_framework import parsers


# Vistas Basadas en Clases Controlando todo el Modelo de Usuarios

class RegisterUsers(generics.CreateAPIView):  # Solo Registrar datos en el modelo
    permission_classes = (permissions.AllowAny,)
    parser_classes = (parsers.JSONParser,)

    def post(self, request, format=None):
        # Creando en Nuevo Usuario
        username = request.data['username']
        email = request.data['email']
        password = request.data['password']
        user = User.objects.create_user(username, email, password)
        user.save()

        # generando el token para ese usuario se refiere a la tabla auth_token
        token = Token.objects.create(user=user)
        data = {'detail': 'User created with token:' + token.key}

        response = json.dumps(data)
        return HttpResponse(response, content_type='application/json')


class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)
    parser_classes = (parsers.JSONParser,)

    def post(self, request, format=None):
        username = request.data["username"]
        password = request.data["password"]
        user = authenticate(username=username, password=password)
        if user:
            
            token = Token.objects.get(user_id=user.id)
            data = {"nombre": user.username,
                    "email": user.email,
                    "token": token.key}
        else:
            data = {"error": "No Son las Credenciales"}
        response = json.dumps(data)
        return HttpResponse(response, content_type='application/json')


class ProductsListView(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = (AllowAny,)


class CompanyAllView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (AllowAny,)

