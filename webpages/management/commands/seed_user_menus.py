from django.core.management.base import BaseCommand
from constants import ROLE_USER
from webpages.models import Menu


class Command(BaseCommand):
    help = "Seed initial menu data with parent-child and roles"

    def handle(self, *args, **kwargs):
        # 一级菜单
        dashboard, _ = Menu.objects.update_or_create(
            title="仪表盘",
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
            title="Sandbox",
            defaults={
                "url": "/sandbox",
                "icon": "fas fa-folder",
                "order": 2,
                "role": ROLE_USER,
                "is_active": True,
                "parent": None,
            },
        )

        settings_menu, _ = Menu.objects.update_or_create(
            title="系统设置",
            defaults={
                "url": "/settings",
                "icon": "fas fa-cog",
                "order": 3,
                "role": ROLE_USER,
                "is_active": True,
                "parent": None,
            },
        )

        # Samples 子菜单
        Menu.objects.update_or_create(
            title="User",
            defaults={
                "url": "/sandbox/user",
                "icon": "far fa-circle",
                "order": 1,
                "role": ROLE_USER,
                "is_active": True,
                "parent": samples_menu,
            },
        )

        # Settings 子菜单
        Menu.objects.update_or_create(
            title="个人资料",
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
            title="安全设置",
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
