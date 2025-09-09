from django.core.management.base import BaseCommand
from constants import ROLE_USER
from webpages.models import Menu


class Command(BaseCommand):
    help = "Seed initial menu data with parent-child and roles"

    def handle(self, *args, **kwargs):
        # 一级菜单
        dashboard, _ = Menu.objects.update_or_create(
            title="Dashboard",
            defaults={
                "url": "/dashboard",
                "icon": "fas fa-tachometer-alt",
                "order": 1,
                "role": ROLE_USER,
                "is_active": True,
                "parent": None,
            },
        )

        samples_menu, _ = Menu.objects.update_or_create(
            title="Samples",
            defaults={
                "url": None,
                "icon": "fas fa-folder",
                "order": 2,
                "role": ROLE_USER,
                "is_active": True,
                "parent": None,
            },
        )

        settings_menu, _ = Menu.objects.update_or_create(
            title="Settings",
            defaults={
                "url": None,  # 一级菜单可无 URL
                "icon": "fas fa-cogs",
                "order": 3,
                "role": ROLE_USER,
                "is_active": True,
                "parent": None,
            },
        )

        # Samples 子菜单
        Menu.objects.update_or_create(
            title="User Sample",
            defaults={
                "url": "/samples/user",
                "icon": "far fa-circle",
                "order": 1,
                "role": ROLE_USER,
                "is_active": True,
                "parent": samples_menu,
            },
        )

        # Settings 子菜单
        Menu.objects.update_or_create(
            title="Profile",
            defaults={
                "url": "/settings/profile",
                "icon": "far fa-circle",
                "order": 1,
                "role": ROLE_USER,
                "is_active": True,
                "parent": settings_menu,
            },
        )

        Menu.objects.update_or_create(
            title="Security",
            defaults={
                "url": "/settings/security",
                "icon": "far fa-circle",
                "order": 2,
                "role": ROLE_USER,
                "is_active": True,
                "parent": settings_menu,
            },
        )

        self.stdout.write(
            self.style.SUCCESS("✅ Initial menu data seeded successfully.")
        )
