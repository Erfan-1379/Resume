from django.contrib import admin
from core.models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')


admin.site.register(CustomUser, UserAdmin)
