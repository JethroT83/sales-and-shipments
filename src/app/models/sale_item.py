from django.db import models
from .sale import Sale

class SaleItem(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name="items")
    sku = models.CharField(max_length=64, db_index=True)
    qty = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)