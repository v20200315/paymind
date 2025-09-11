from rest_framework import serializers

from accounts.models import CustomUser
from sandbox.models import Product, Customer


class ProductSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source="get_status_display")
    type = serializers.CharField(source="get_type_display")
    created_by = serializers.SerializerMethodField()
    updated_by = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = "__all__"

    def get_created_by(self, obj):
        if not obj.created_by:
            return None
        try:
            user = CustomUser.objects.get(pk=obj.created_by)
            return user.email
        except CustomUser.DoesNotExist:
            return None

    def get_updated_by(self, obj):
        if not obj.updated_by:
            return None
        try:
            user = CustomUser.objects.get(pk=obj.updated_by)
            return user.email
        except CustomUser.DoesNotExist:
            return None


class CustomerSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source="get_status_display")
    created_by = serializers.SerializerMethodField()
    updated_by = serializers.SerializerMethodField()

    class Meta:
        model = Customer
        fields = "__all__"

    def get_created_by(self, obj):
        if not obj.created_by:
            return None
        try:
            user = CustomUser.objects.get(pk=obj.created_by)
            return user.email
        except CustomUser.DoesNotExist:
            return None

    def get_updated_by(self, obj):
        if not obj.updated_by:
            return None
        try:
            user = CustomUser.objects.get(pk=obj.updated_by)
            return user.email
        except CustomUser.DoesNotExist:
            return None
