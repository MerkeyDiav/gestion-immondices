from rest_framework import generics
from rest_framework.response import Response

from .serializers import (
    ResidentSerializer,
    SignalementSerializer,
    NotificationSerializer,
)
from .models import Signalement, Notification


class CreateUserView(generics.CreateAPIView):
    serializer_class = ResidentSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)


class SignalementList(generics.ListCreateAPIView):
    serializer_class = SignalementSerializer
    queryset = Signalement.objects.all()


class SignalementDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Signalement.objects.all()
    serializer_class = SignalementSerializer


class CreateNotificationView(generics.CreateAPIView):
    serializer_class = NotificationSerializer
    # permission_classes = permissions.
    queryset = Notification.objects.all()


class NotificationListAPIView(generics.ListAPIView):
    serializer_class = NotificationSerializer

    def get_queryset(self):
        user = self.request.user
        return Notification.objects.filter(user=user, is_read=False)

    def perform_update(self, serializer):
        serializer.save(is_read=True)
