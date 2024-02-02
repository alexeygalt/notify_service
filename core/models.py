from django.contrib.auth.models import AbstractUser
from django.db import models
from core.managers import UserManager


class User(AbstractUser):
    class AuthProvider(models.TextChoices):
        GOOGLE = "facebook", "facebook"
        FACEBOOK = "google", "google"
        EMAIL = "email", "email"

    email = models.EmailField(
        "email address",
        blank=True,
        unique=True,
    )
    username = models.CharField(max_length=32, null=True, blank=True, unique=False)
    auth_provider = models.CharField(
        max_length=32,
        blank=False,
        null=False,
        default=AuthProvider.EMAIL,
        verbose_name="Провайдер",
    )

    objects = UserManager()
    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = []

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"{self.id} - {self.email}"
