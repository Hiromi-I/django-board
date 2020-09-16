from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    class Meta(AbstractUser.Meta):
        db_table = 'custom_user'

    def __str__(self):
        return self.username
