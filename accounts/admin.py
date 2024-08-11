from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreation, CustomChangeCreation
# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreation
    form = CustomChangeCreation
    model = CustomUser
    list_display = ('email','username', 'first_name', 'last_name', 'age', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets +(
        (None, {'fields': ('age',)}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
