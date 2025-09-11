from django.urls import path, include
from rest_framework.routers import DefaultRouter

from sandbox.views import (
    ProductDataTablesView,
    ProductViewSet,
    CustomerViewSet,
    CustomerDataTablesView,
)

router = DefaultRouter()
router.register(r"products", ProductViewSet, basename="product")
router.register(r"customers", CustomerViewSet, basename="customer")

urlpatterns = [
    path("", include(router.urls)),
    path(
        "product/datatables/",
        ProductDataTablesView.as_view(),
        name="product_datatables",
    ),
    path(
        "customer/datatables/",
        CustomerDataTablesView.as_view(),
        name="customer_datatables",
    ),
]
