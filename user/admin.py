from django.contrib import admin
from .models import User,Contact

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('username','email','password')
    list_filter = ('username','email','password')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('owner','contact','phone_number')
    list_filter = ('owner','contact','phone_number')


admin.site.register(User,UserAdmin)
admin.site.register(Contact,ContactAdmin)
