from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import MemberManager
from django.utils import timezone

# Create your models here.
class Member(PermissionsMixin, AbstractBaseUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=150)

    home_address = models.OneToOneField("address.Address", on_delete=models.CASCADE, null=True, blank=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS=['name']

    objects = MemberManager()

    def __str__(self):
        return self.email