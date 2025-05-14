from django.contrib import admin
from .models import Grade


# Register your models here.

class GradeAdmin(admin.ModelAdmin):
    list_display = ('name', 'grade')
    search_fields = ('name', 'grade')
    list_filter = ('grade',)

    def has_add_permission(self, request):
        return False


admin.site.register(Grade)
