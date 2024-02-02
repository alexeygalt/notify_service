from django.urls import path

from client.views import CreateClientView, UpdateClient

urlpatterns = [
    path("create_client/", CreateClientView.as_view(), name="create_client"),
    path("<int:pk>/", UpdateClient.as_view(), name="update_delete_client"),
    ]