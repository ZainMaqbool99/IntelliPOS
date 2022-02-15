
from rest_framework import serializers
import Inventory.models as Models

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Models.Category
        fields = (
            'CId',
            'CName',
            'isActive'
        )

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Models.Brands
        fields = (
            'BId',
            'BName',
            'isActive'
        )

class ItemSetupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Models.ItemSetup
        fields = '__all__'

class OpeningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Models.Opening
        fields = '__all__'

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Models.Purchase
        fields = '__all__'

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Models.Stock
        fields = '__all__'
