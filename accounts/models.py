import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)  # 每个用户邮箱唯一
    phone = models.CharField(max_length=20, blank=True, null=True, unique=True)
    role = models.ForeignKey(
        "Role", on_delete=models.SET_NULL, null=True, blank=True, related_name="users"
    )

    def __str__(self):
        return self.email


class Role(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
