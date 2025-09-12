from django.contrib import admin
from django import forms
from accounts.models import CustomUser
from .models import Company, Employee, Payroll


class CompanyAdminForm(forms.ModelForm):
    created_by = forms.ModelChoiceField(
        queryset=CustomUser.objects.all(),
        required=False,
        label="Created By",
    )
    updated_by = forms.ModelChoiceField(
        queryset=CustomUser.objects.all(),
        required=False,
        label="Updated By",
    )

    class Meta:
        model = Company
        fields = "__all__"

    def clean_created_by(self):
        user = self.cleaned_data.get("created_by")
        return user.id if user else None

    def clean_updated_by(self):
        user = self.cleaned_data.get("updated_by")
        return user.id if user else None


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    form = CompanyAdminForm
    list_display = ("name", "owner", "status", "created_at", "updated_at")
    list_filter = ("status", "created_at")
    search_fields = ("name", "owner__username", "owner__email")
    ordering = ("-created_at",)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("name", "company", "email", "phone", "hire_date", "status")
    list_filter = ("status", "hire_date", "company")
    search_fields = ("name", "email", "phone", "company__name")
    ordering = ("-hire_date",)


@admin.register(Payroll)
class PayrollAdmin(admin.ModelAdmin):
    list_display = (
        "employee",
        "month",
        "base_salary",
        "bonus",
        "social_security",
        "housing_fund",
        "created_at",
    )
    list_filter = ("month", "employee__company")
    search_fields = ("employee__name", "employee__company__name")
    date_hierarchy = "month"
    ordering = ("-month",)
