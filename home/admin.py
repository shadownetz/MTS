from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    model = User

    list_display = (
        'id', 'email', 'name', 'phone', 'address', 'password', 'is_active',
        'is_staff', 'is_superuser', 'last_login', 'created_at',
        'avatar', 'updated_at'
    )

    fieldsets = (
        (None, {
            'fields': (
                'email', 'name', 'phone', 'address', 'is_active',
                'is_staff', 'is_superuser', 'avatar',
            )
        }),
    )

    ordering = ('id', 'created_at')


admin.site.register(User, UserAdmin)
