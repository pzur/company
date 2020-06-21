from django.urls import path, include
from . import views
from .views import ProductsCreat
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Products', ProductsCreat)

urlpatterns = [
    path('Registeruser/', views.RegisterUsers.as_view()),
    path('Login/', views.LoginView.as_view()),
    path('Users/', views.UserListView.as_view()),
    path('Companys/', views.CompanyAllView.as_view()),
    path('',include(router.urls)),
    path('Logout/',views.LogoutView.as_view()),
]

#http://127.0.0.1:8000/Registeruser/  para registrar
#http://127.0.0.1:8000/Login/  para logearte
#http://127.0.0.1:8000/Logut/  para logearte
#http://127.0.0.1:8000/Companys/  para ver Compañias
#http://127.0.0.1:8000/Products/  CRUD de los productos GET POST PUT PATCH
#http://127.0.0.1:8000/Users/  para ver todos los usuarios