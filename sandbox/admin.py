from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "price",
        "stock",
        "status",
        "type",
        "created_by",
        "updated_by",
        "created_at",
        "updated_at",
    )
    list_filter = ("status", "type", "created_at", "updated_at")
    search_fields = ("name", "slug", "description")
    ordering = ("-created_at",)
    readonly_fields = ("created_at", "updated_at")

    fieldsets = (
        (
            "Basic Info",
            {
                "fields": (
                    "name",
                    "description",
                    "price",
                    "stock",
                    "status",
                    "type",
                )
            },
        ),
        (
            "Audit Info",
            {"fields": ("created_by", "updated_by", "created_at", "updated_at")},
        ),
    )
