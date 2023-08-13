# serializer to add catergories for invertory items
from rest_framework import serializers

from .models import InventoryCaterogorie

class InventoryCatergorySerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryCaterogorie
        fields = ("inverntory_category_id", "name", "description", "date_created", "date_modified")
        required_fields = ("name",)
        read_only_fields = ("inverntory_category_id", "date_created", "date_modified")                                                