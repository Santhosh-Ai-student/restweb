from django.contrib import admin
from .models import UserDetails, OrderDetails

@admin.register(UserDetails)
class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ("user", "phone")


@admin.register(OrderDetails)
class OrderDetailsAdmin(admin.ModelAdmin):
    list_display = ("user", "food_name", "price", "order_time")
    list_filter = ("order_time",)
