from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(
        self,
        email,
        password=None,
        username=None,
        first_name=None,
        last_name=None,
        phone=None,
    ):
        if not email:
            raise ValueError("User must have a email ")
        user = self.model(
            email=self.normalize_email(email),
        )
        user.username = username
        user.is_active = True
        user.is_staff = True
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password=None):
        user = self.model(
            email=email,
            password=password,
        )
        user.is_active = True
        user.is_superuser = True
        user.is_staff = True
        user.set_password(user.password)
        user.save(using=self._db)

        return user
