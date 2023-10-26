from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Notification
from waste.models import Collecte


# @receiver(post_save, sender=Collecte)
# def create_notification(sender, instance, created, **kwargs):
#     if created:
#         residents = instance.residents.all()
#         residents_str = str(residents)
#         print(f"la liste des residents recuperées : {residents_str}")
#         for resident in residents:
#             content = f"Vous avez été concerné dans une collecte pour ce {instance.date_collecte}."
#             notification = Notification(user=resident.user, content=content)
#             notification.save()


from django.db.models.signals import m2m_changed


@receiver(m2m_changed, sender=Collecte.residents.through)
def collecte_residents_changed(sender, instance, action, **kwargs):
    if action == "post_add":
        residents = instance.residents.all()
        print("Résidents récupérés :", residents)
        for resident in residents:
            content = f"Vous avez été concerné dans une collecte pour ce {instance.date_collecte}."
            notification = Notification(user=resident, content=content)
            notification.save()
