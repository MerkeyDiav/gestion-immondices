from django.urls import path
from .views import (
    CreateUserView,
    SignalementList,
    SignalementDetail,
    NotificationListAPIView,
)

urlpatterns = [
    path("registration/", CreateUserView.as_view(), name="resident_registration"),
    path("signalement/list/", SignalementList.as_view(), name="signalement_list"),
    path(
        "signalement/<int:pk>/", SignalementDetail.as_view(), name="signalement_detail"
    ),
    path("notifications/", NotificationListAPIView.as_view(), name="notification_list"),
]
