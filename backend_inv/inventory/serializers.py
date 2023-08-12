# serializer to add catergories for invertory items
from rest_framework import serializers

from .models import InventoryCaterogorie

class CatergorySerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryCaterogorie
        fields = ('category_id', 'name', 'description', 'date_created', 'date_modified')