from typing import Iterable, Optional, List
from rest_framework.exceptions import AuthenticationFailed
from core.social_auth.utils import password_generator
from rest_framework_simplejwt.tokens import RefreshToken
from core.models import User


class UserDAO:
    """Base class for working with a User model"""

    def get_user_by_id(self, id: int) -> Optional[User]:
        if not User.objects.filter(id=id).exists():
            return None
        return User.objects.get(id=id)

    def get_all_users(self) -> List[User]:
        return User.objects.all()

    def update_is_active(self, users_ids: Iterable[int], is_active: bool) -> None:
        pass

    @staticmethod
    def _create_social_user(email: str, provider: str, password: str) -> User:
        # user = User.objects.create_user(email=email, password=env.str('SOCIAL_SECRET'))
        user = User.objects.create_user(email=email, password=password)
        user.is_active = True
        user.auth_provider = provider
        user.save()
        return user

    @staticmethod
    def _get_tokens_for_user(user_orm: User) -> dict:
        refresh = RefreshToken.for_user(user_orm)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }

    @staticmethod
    def register_social_user(provider, email) -> dict:
        user = User.objects.filter(email=email).first()
        if user:
            if provider == user.auth_provider:
                return {
                    "email": user.email,
                    "tokens": UserDAO._get_tokens_for_user(user),
                }
            else:
                raise AuthenticationFailed(
                    detail="Please continue your login using " + user.auth_provider
                )

        else:
            user_password = password_generator()
            user = UserDAO._create_social_user(
                email=email, provider=provider, password=user_password
            )
            return {
                "email": user.email,
                "password": user_password,
                "tokens": UserDAO._get_tokens_for_user(user),
            }
