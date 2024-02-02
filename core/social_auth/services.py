from abc import ABC, abstractmethod
from google.auth.transport.requests import Request
from google.oauth2 import id_token
import facebook
from rest_framework.exceptions import ValidationError


class OAuthService(ABC):
    @staticmethod
    @abstractmethod
    def validate(auth_token: str):
        pass


class Google(OAuthService):
    """Класс Google для получения информации о пользователе и ее возврата"""

    @staticmethod
    def validate(auth_token: str):
        """
        Метод проверки токена. Запрашивает API Google oAUTH2 для получения информации о пользователе.
        """
        try:
            id_info = id_token.verify_oauth2_token(auth_token, Request())

            if "accounts.google.com" in id_info["iss"]:
                return id_info

        except Exception:
            return "Токен недействителен, либо срок его действия истек."


class Facebook(OAuthService):
    """
    Класс Facebook для получения информации о пользователе и ее возврата
    """

    @staticmethod
    def validate(auth_token: str):
        """
        Метод проверки токена . Запрашивает Facebook GraphAPI для получения информации о пользователе.
        """

        graph = facebook.GraphAPI(access_token=auth_token)

        try:
            profile = graph.request("/me?fields=name,email")
        except facebook.GraphAPIError:
            raise ValidationError("Токен недействителен, либо срок его действия истек.")

        return profile
