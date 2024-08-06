from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    products = Product.objects.all()
    context = {"products_Key":products}
    return render(request, 'home.html', context)

def about(request):
    context = {"contacts":contacts}
    return render(request, 'about.html', context)

def arrangements(request):
 
    context = {}
    return render(request, 'arrangements.html', context)

def flower(request):
    products = Product.objects.all()
    context = {"products_Key":products}
    return render(request, 'flower.html', context)

def wedding(request):
    contacts = FormContact.objects.all()
    context = {"contacts":contacts}
    return render(request, 'wedding.html', context)


def contact(request):
    if request.method == "POST":
        name = request.POST['firstName']
        surname = request.POST['lastName']
        email = request.POST['email']
        comment = request.POST['comment']
        if name !="" and surname !="" and email !="" and comment != "":
            FormContact(
                formContact_name = name,
                formContact_surname = surname,
                formContact_email = email,
                formContact_comment = comment
            ).save()
            messages.success(request, 'Message sended!!!')
        else:
            messages.error(request, 'Message not sended!!!')
    context = {}
    return render(request, 'contact.html', context)

# def detailProduct(request, id):
#     productDetail = Product.objects.get(pk=id)
#     context = {"productDetail":productDetail}
#     return render(request, 'detailProduct.html', context)

def detailProduct(request, slug):
    productDetail = Product.objects.get(product_slug=slug)
    context = {"productDetail":productDetail}
    return render(request, 'detailProduct.html', context)

def detailCategory(request, id):
    categoryDetail = Category.objects.get(pk=id)
    categoryProducts = Product.objects.filter(product_category=categoryDetail)
    context = {"categoryDetail": categoryDetail, "categoryProducts": categoryProducts }
    return render(request, "detailCategory.html", context)


# Auth
# Funksioni i regjistrimit
def register(request):
    context = {"cat": categories}
    # Marrja e informacioneve
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]
        # Kontrollohet nese passwordet jane te njejte
        if (
            first_name == ""
            and last_name == ""
            and username == ""
            and email == ""
            and password == ""
            and confirm_password == ""
        ):
            return redirect("../register/")
        else:
            if password == confirm_password:
                # Kontrollohet nese useri eshte regjistruar me pare
                if User.objects.filter(username=username).exists():
                    # nese po behet rifresh faqja e regjister
                    return redirect("/")
                else:
                    # Krijohet nje user i ri
                    user = User.objects.create_user(
                        email=email,
                        username=username,
                        password=password,
                        first_name=first_name,
                        last_name=last_name,
                    )
                    user.set_password(password)
                    # Ruhet useri
                    user.save()
                    # kalon tek faqja e login
                    return redirect("../login/")
    else:
        return render(request, "auth/register.html", context)


def login(request):
    context = {"categories": categories}
    # marrja e te dhenave nga forma
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        # Kontrollo i te dhenave
        user = auth.authenticate(username=username, password=password)
        # Nese logohet kalon tek faqja e homh
        if user is not None:
            # metode e djangos
            auth.login(request, user)
            return redirect("/")
        else:
            # nese nuk perputhen informacionet behet refresh faqja
            return redirect("login/")
    else:
        return render(request, "auth/login.html", context)


# funksioni i logout
def logout(request):
    # metode e django-s
    auth.logout(request)
    return redirect("/")


# Nuk e akseson faqen nese nuk je i log-uar
@login_required(login_url="/login/")
def accessLogin(request):
    context = {"categories": categories}
    return render(request, "accessLogin.html", context)