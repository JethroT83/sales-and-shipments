from rest_framework import viewsets, serializers
from app.models.sale import Sale
from app.models.sale_item import SaleItem

class SaleItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleItem
        fields = ("sku","qty","unit_price")

class SaleSerializer(serializers.ModelSerializer):
    items = SaleItemSerializer(many=True)
    class Meta:
        model = Sale
        fields = ("id","customer","status","total","idempotency_key","items","created_at")
        read_only_fields = ("id","status","total","created_at")

    def create(self, validated):
        items = validated.pop("items", [])
        sale = Sale.objects.create(**validated)
        for i in items:
            SaleItem.objects.create(sale=sale, **i)
        # enqueue async processing here if you want
        return sale

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all().select_related("customer").prefetch_related("items")
    serializer_class = SaleSerializer
