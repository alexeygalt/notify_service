from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from core.social_auth.views import GoogleSocialAuthView, FacebookSocialAuthView
from core.views import UserRegistrationView, GetMe

urlpatterns = [
    path(
        "register/", UserRegistrationView.as_view(), name="signup"
    ),
    path(
        "me/", GetMe.as_view(), name="me"
    ),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("login/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path('google/', GoogleSocialAuthView.as_view()),
    path('facebook/', FacebookSocialAuthView.as_view()),
]