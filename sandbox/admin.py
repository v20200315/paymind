from django.contrib import admin
from .models import Product, Customer


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
    search_fields = ("name", "description")
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


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "email",
        "phone",
        "status",
        "created_by",
        "updated_by",
        "created_at",
        "updated_at",
    )
    list_filter = ("status", "created_at", "updated_at")
    search_fields = ("name",)
    ordering = ("-created_at",)
    readonly_fields = ("created_at", "updated_at")

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "email", "phone", "status")},
        ),
        (
            "Audit Info",
            {"fields": ("created_by", "updated_by", "created_at", "updated_at")},
        ),
    )
