# apps/menu/admin.py
from django.contrib import admin
from .models import Menu


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    # 列表显示的字段
    list_display = ("title", "url", "icon", "parent", "role", "order", "is_active")
    # 可以在列表页直接编辑的字段
    list_editable = ("order", "is_active")
    # 支持按角色和激活状态过滤
    list_filter = ("role", "is_active", "parent")
    # 支持按 title 或 URL 搜索
    search_fields = ("title", "url")
    # 默认排序
    ordering = ("order",)
    # 表单布局优化（可选）
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "title",
                    "url",
                    "icon",
                    "parent",
                    "role",
                    "order",
                    "is_active",
                )
            },
        ),
    )
