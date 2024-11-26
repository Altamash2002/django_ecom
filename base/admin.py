from django.contrib import admin
from .models import CustomUser,Category,Cart,Product,CartItem

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(Product)
admin.site.register(CartItem)