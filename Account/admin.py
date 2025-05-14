from django.contrib import admin

from .models import User


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email')
    list_display_links = ('id', 'username', 'email')
    search_fields = ('id', 'username', 'email')
    # list_filter = ('is_active', 'is_staff', 'is_superuser')

    def has_add_permission(self, request):
        return False


admin.site.register(User)
