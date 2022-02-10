from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin



class AccountAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name',  'is_active')
    filter_horizontal = ()
    list_filter =()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)
