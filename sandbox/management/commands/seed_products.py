import uuid
import random

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from faker import Faker
from sandbox.models import Product


class Command(BaseCommand):
    help = "Seed the database with 100 sample products"

    def handle(self, *args, **kwargs):
        fake = Faker("zh_CN")

        User = get_user_model()
        users = list(User.objects.all())
        if not users:
            raise Exception(
                "No users found. Please create at least one user (e.g., via createsuperuser)."
            )

        products = []

        STATUS_CHOICES = ["draft", "active", "inactive"]
        TYPE_CHOICES = ["physical", "digital", "service"]

        for _ in range(100):
            name = fake.word() + fake.word()
            description = fake.text(max_nb_chars=100)

            product = Product(
                id=uuid.uuid4(),
                name=name,
                description=description,
                price=round(random.uniform(10.0, 999.99), 2),
                stock=random.randint(0, 500),
                status=random.choice(STATUS_CHOICES),
                type=random.choice(TYPE_CHOICES),
                created_by=random.choice(users).id,
                updated_by=random.choice(users).id,
            )
            products.append(product)

        Product.objects.bulk_create(products, batch_size=50)
        self.stdout.write(self.style.SUCCESS("Successfully seeded 100 products"))
