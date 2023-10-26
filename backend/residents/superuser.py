from django.contrib.auth import get_user_model

User = get_user_model()
superuser = User.objects.create_superuser(
    username="adminUser1",
    password="adminUserPassword",
    first_name="immacule",
    street="elungu",
    postal_number=82,
    born_date="2003-01-01",
)
