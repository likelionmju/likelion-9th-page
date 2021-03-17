from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class LikelionUserManager(BaseUserManager):

    def create_user(self, pk, extra_data):
        user = LikelionUser.objects.get(pk=pk)
        user.name = extra_data["name"]
        user.img = extra_data["picture"]
        user.save()
        return user


# Create your models here.
class LikelionUser(AbstractBaseUser):
    class Meta:
        db_table = "likelion_user"

    is_active = True
    is_admin = False
    is_superuser = False
    is_staff = False

    name = models.CharField(max_length=40, null=False, default="")
    img = models.URLField(default="")

    email = models.EmailField()
    username = models.CharField(max_length=40, null=False, unique=True)

    objects = LikelionUserManager()

    USERNAME_FIELD = "username"
