from django.urls import path

from .views import (
    CollecteList,
    CollecteDetail,
    ContainerDetail,
    CollectPointDetail,
    ContainerList,
    CollectPointList,
)

urlpatterns = [
    path("collecte/list/", CollecteList.as_view(), name="collecte_list"),
    path("container/list/", ContainerList.as_view(), name="container_list"),
    path("collect-point/list/", CollectPointList.as_view(), name="collecte_point_list"),
    path("collecte/<int:pk>/", CollecteDetail.as_view(), name="collecte_detail"),
    path("container/<int:pk>/", ContainerDetail.as_view(), name="container_detail"),
    path(
        "container/<int:pk>/",
        CollectPointDetail.as_view(),
        name="collecte_point_detail",
    ),
    # path("collecte"),
]
