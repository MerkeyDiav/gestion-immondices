# from django.contrib.auth.forms import UserCreationForm
# from .models import Résident

# class CustomUserCreationForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         model = Résident

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         # Supprimez les champs que vous ne souhaitez pas afficher pour la création du superutilisateur
#         del self.fields['champ1']
#         del self.fields['champ2']
#         # Ajoutez d'autres champs si nécessaire