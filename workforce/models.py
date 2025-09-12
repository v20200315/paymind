import uuid
from django.db import models
from django.conf import settings
from common.models import TimeStampedModel, StatusModel


class Company(StatusModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="companies",
    )
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Employee(StatusModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="employees"
    )
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    hire_date = models.DateField()

    def __str__(self):
        return f"{self.name} ({self.company.name})"


class Payroll(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name="payrolls"
    )
    base_salary = models.DecimalField(max_digits=10, decimal_places=2)
    bonus = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    social_security = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    housing_fund = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    month = models.DateField(help_text="工资对应月份，例如 2025-09-01")

    def __str__(self):
        return f"{self.employee.name} - {self.month.strftime('%Y-%m')}"
