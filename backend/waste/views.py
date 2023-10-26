from django.shortcuts import render
from rest_framework import generics

from .models import Collecte, CollectPoint, Container
from .serializers import CollecteSerializer, ContainerSerializer, CollectPointSerializer


class CollecteList(generics.ListCreateAPIView):
    queryset = Collecte.objects.all()
    serializer_class = CollecteSerializer


class CollecteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Collecte.objects.all()
    serializer_class = CollecteSerializer


class CollectPointList(generics.ListCreateAPIView):
    queryset = CollectPoint.objects.all()
    serializer_class = CollectPointSerializer


class CollectPointDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CollectPoint.objects.all()
    serializer_class = CollectPointSerializer


class ContainerList(generics.ListCreateAPIView):
    queryset = Container.objects.all()
    serializer_class = ContainerSerializer


class ContainerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Container.objects.all()
    serializer_class = ContainerSerializer
