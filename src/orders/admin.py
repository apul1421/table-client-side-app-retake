from django.contrib import admin

# Register your models here.

from .models import UserCheckout, Order

admin.site.register(UserCheckout)

admin.site.register(Order)

#admin.site.register()