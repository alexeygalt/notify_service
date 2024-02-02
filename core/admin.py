from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.urls import reverse
from core.models import User
from django.utils.safestring import mark_safe


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ("id", "email_link", "auth_provider",)
    search_fields = (
        "email__startswith",
        "id",
    )
    list_filter = ("auth_provider",)
    ordering = (
        "auth_provider",
    )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "username",
                    "auth_provider",
                    "is_staff",
                    "is_active",
                    "date_joined",
                    "last_login",

                )
            },
        ),
        ("Change password", {"classes": ("collapse",), "fields": ("password",)}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )

    def email_link(self, user: User):
        url = reverse("admin:core_user_change", args=[user.id])
        link = '<a href="%s">%s</a>' % (url, user.email)
        return mark_safe(link)

    email_link.short_description = "Адрес электронной почты"
