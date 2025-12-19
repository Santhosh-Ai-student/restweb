# restaurant_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_view, name="login"),
    path("signup/", views.signup_view, name="signup"),
    path("home/", views.home, name="home"),
    path("add/<int:food_id>/", views.add_to_cart),
    path("order/", views.place_order),
    path("logout/", views.logout_view),
]
