import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

from constants import ORG_ROLE_CHOICES, ADMIN_ROLES, ROLE_USER, ROLE_MEMBER, ROLE_OWNER


class Organization(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_owner(self):
        """获取组织的 OWNER 用户"""
        membership = self.memberships.filter(role=ROLE_OWNER).first()
        return membership.user if membership else None


class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)  # 每个用户邮箱唯一
    phone = models.CharField(max_length=20, blank=True, null=True, unique=True)

    def __str__(self):
        return self.email

    def get_role(self, organization):
        """获取用户在指定组织下的角色"""
        membership = self.memberships.filter(organization=organization).first()
        return membership.role if membership else ROLE_USER

    def get_default_role(self):
        return ROLE_USER

    def is_admin(self, organization):
        """是否在某组织下为 ADMIN 或 OWNER"""
        role = self.get_role(organization)
        return role in ADMIN_ROLES


class Membership(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    organization = models.ForeignKey(
        Organization, on_delete=models.CASCADE, related_name="memberships"
    )
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="memberships"
    )
    role = models.CharField(
        max_length=20, choices=ORG_ROLE_CHOICES, default=ROLE_MEMBER
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("organization", "user")

    def __str__(self):
        return f"{self.user.username} in {self.organization.name} as {self.role}"
