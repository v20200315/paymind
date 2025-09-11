from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Product, Customer
from .pagination import DataTablesPagination
from .serializers import ProductSerializer, CustomerSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ProductDataTablesView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = DataTablesPagination
    search_fields = ["name", "description", "type", "status"]
    ordering_fields = [
        "id",
        "name",
        "description",
        "price",
        "stock",
        "status",
        "type",
        "created_at",
        "created_by",
        "updated_at",
        "updated_by",
    ]

    def get(self, request, *args, **kwargs):
        queryset = Product.objects.all()
        paginator = self.pagination_class()
        paginated_qs = paginator.paginate_queryset(queryset, request, view=self)
        serializer = ProductSerializer(paginated_qs, many=True)
        return paginator.get_paginated_response(serializer.data)


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CustomerDataTablesView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = DataTablesPagination
    search_fields = ["name", "email", "phone", "status"]
    ordering_fields = [
        "id",
        "name",
        "email",
        "phone",
        "status",
        "created_at",
        "created_by",
        "updated_at",
        "updated_by",
    ]

    def get(self, request, *args, **kwargs):
        queryset = Customer.objects.all()
        paginator = self.pagination_class()
        paginated_qs = paginator.paginate_queryset(queryset, request, view=self)
        serializer = CustomerSerializer(paginated_qs, many=True)
        return paginator.get_paginated_response(serializer.data)
