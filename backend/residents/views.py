from rest_framework import generics
from rest_framework.response import Response
from .serializers import ResidentSerializer


class CreateUserView(generics.CreateAPIView):
    serializer_class = ResidentSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)
