from django.urls import path
from . import views

urlpatterns =[
    path('',views.home, name="homePage"),
    path('about/',views.about, name="aboutPage"),
    path('contact/', views.contact, name="contactPage"),
    # path('detailProduct/<id>', views.detailProduct, name="detailProductPage")
    path('detailProduct/<slug>', views.detailProduct, name="detailProductPage"),
    path('detailCategory/<id>', views.detailCategory, name="detailCategoryPage"),
    # Auth
    path("register/", views.register, name="registerPage"),
    path("login/", views.login, name="loginPage"),
    path("logout/", views.logout, name= "logout"),
    path("accessLogin/", views.accessLogin, name= "accessLoginPage"),
]