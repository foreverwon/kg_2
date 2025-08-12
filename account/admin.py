from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "username", "role", "is_active", "is_staff", "date_joined", "last_login")
    list_filter = ("role", "is_active", "is_staff")
    search_fields = ("email", "username")