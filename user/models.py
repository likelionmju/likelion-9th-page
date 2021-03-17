from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class LikelionUserManager(BaseUserManager):

    def get_or_create_user(self, pk, extra_data):
        user = LikelionUser.objects.get(pk=pk)
        user.name = extra_data["name"]
        user.img = extra_data["picture"]
        user.save()
        return user

    def create_superuser(self, username, password):
        user = self.model(username=username)
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


# Create your models here.
class LikelionUser(AbstractBaseUser, PermissionsMixin):
    class Meta:
        db_table = "likelion_user"

    is_active = models.BooleanField(null=False, default=True)
    is_superuser = models.BooleanField(null=False, default=False)
    is_staff = models.BooleanField(null=False, default=False)

    name = models.CharField(max_length=40, null=False, default="")
    img = models.URLField(default="")

    email = models.EmailField()
    username = models.CharField(max_length=40, null=False, unique=True)

    objects = LikelionUserManager()

    USERNAME_FIELD = "username"
