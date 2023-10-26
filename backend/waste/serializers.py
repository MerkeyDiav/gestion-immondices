from rest_framework import serializers
from .models import Collecte, CollectPoint, Container


class CollecteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collecte
        fields = "__all__"


class CollectPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectPoint
        fields = "__all__"


class ContainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Container
        fields = "__all__"
