from django.urls import path
from . import views

urlpatterns = [
    path('Registeruser/', views.RegisterUsers.as_view()),
    path('Login/', views.LoginView.as_view()),
    path('Companys/', views.CompanyAllView.as_view()),
    path('ProductsAll/',views.ProductsListView.as_view()),
]

#http://127.0.0.1:8000/Registeruser/  para registrar
#http://127.0.0.1:8000/Login/  para logearte