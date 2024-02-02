from django.urls import path
from mailing.views import CreateMailingView, UpdateMailing, MailingListView
from message.views import SentMessagesByMailingList

urlpatterns = [
    path("create_mailing/", CreateMailingView.as_view(), name="create_mailing"),
    path("<int:pk>/", UpdateMailing.as_view(), name="update_delete_mailing"),
    path(
        "<int:pk>/messages",
        SentMessagesByMailingList.as_view(),
        name="all_messages_by_mailing",
    ),
    path("", MailingListView.as_view(), name="list_all_mailing"),
]
