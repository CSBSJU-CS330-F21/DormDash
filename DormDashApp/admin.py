from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

admin.site.register(User,UserAdmin)
admin.site.register(Restaurant)
admin.site.register(Order)
#admin.site.register(menuItem)
#admin.site.register(OrderDetails)