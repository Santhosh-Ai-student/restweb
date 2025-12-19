# restaurant_app/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import UserDetails, OrderDetails


FOODS = [
    {"id":1,"name":"Idli","price":40,"img":"images/idly.jpg"},
    {"id":2,"name":"Dosa","price":60,"img":"images/dosa.jpg"},
    {"id":3,"name":"Pongal","price":50,"img":"images/pongal.jpg"},
    {"id":4,"name":"Vada","price":30,"img":"images/vada.jpg"},
    {"id":5,"name":"Poori","price":45,"img":"images/poori.jpg"},
    {"id":6,"name":"Parotta","price":50,"img":"images/parota.jpg"},
    {"id":7,"name":"Pizza","price":150,"img":"images/pizza.jpg"},
    {"id":8,"name":"Burger","price":120,"img":"images/burger.png"},
]


def signup_view(request):
    if request.method == "POST":
        user = User.objects.create_user(
            username=request.POST["username"],
            password=request.POST["password"]
        )
        UserDetails.objects.create(user=user, phone=request.POST["phone"])
        login(request, user)   # 🔥 auto-login
        return redirect("home")
    return render(request, "signup.html")

def login_view(request):
    if request.method == "POST":
        user = authenticate(
            username=request.POST["username"],
            password=request.POST["password"]
        )
        if user:
            login(request, user)
            return redirect("home")
        return render(request, "login.html", {"error":"Invalid credentials"})
    return render(request, "login.html")

@login_required
def home(request):
    cart = request.session.get("cart", [])
    return render(request, "home.html", {"foods": FOODS, "cart": cart})

@login_required
def add_to_cart(request, food_id):
    cart = request.session.get("cart", [])
    for food in FOODS:
        if food["id"] == food_id:
            cart.append(food)
            break
    request.session["cart"] = cart
    return redirect("home")

@login_required
def place_order(request):
    cart = request.session.get("cart", [])
    total = 0
    for item in cart:
        OrderDetails.objects.create(
            user=request.user,
            food_name=item["name"],
            price=item["price"]
        )
        total += item["price"]
    request.session["cart"] = []
    return render(request, "bill.html", {"cart": cart, "total": total})

def logout_view(request):
    logout(request)
    return redirect("login")
