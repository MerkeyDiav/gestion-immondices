from django.db import models
from django.urls import reverse


STATE = (
    ("en_attente", "en attente"),
    ("en_cours", "En cours"),
    ("terminee", "Terminée"),
)

CONTAINER_STATE = (
    (1, "plein"),
    (2, "intermediaire"),
    (3, "vide"),
)

WASTE_TYPE = (
    (1, "organique"),
    (2, "plastique"),
    (3, "radioactif"),
)


class Container(models.Model):
    capacity = models.IntegerField()
    state = models.CharField(max_length=20, choices=CONTAINER_STATE, default=3)
    waste_type = models.CharField(max_length=20, choices=WASTE_TYPE, default=1)

    def __str__(self):
        pass

    class Meta:
        db_table = ""
        managed = True
        verbose_name = "Container"
        verbose_name_plural = "Containers"


class Collecte(models.Model):
    date_collecte = models.DateField()
    collect_state = models.CharField(max_length=20, choices=STATE, default="en_attente")
    collect_point = models.ForeignKey("waste.CollectPoint", on_delete=models.CASCADE)
    residents = models.ManyToManyField(
        "residents.Resident", related_name="resident_included_in_the_collect"
    )

    def __str__(self):
        return f"collecte du {self.date_collecte}"

    class Meta:
        db_table = ""
        managed = True
        verbose_name = "Collecte"
        verbose_name_plural = "Collectes"


class CollectPoint(models.Model):
    name = models.CharField(max_length=30)
    adress = models.CharField(max_length=50)
    state = models.CharField(max_length=30, choices=STATE, default="en_attente")

    class Meta:
        verbose_name = "collectpoint"
        verbose_name_plural = "collectpoints"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("collectpoint_detail", kwargs={"pk": self.pk})
