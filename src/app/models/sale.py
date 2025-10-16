from django.db import models
from uuid import uuid4
from support.helpers import generate_idempotency_key
from .customer import Customer

class Sale(models.Model):
    class Status(models.TextChoices):
        NEW = "new", "New"
        PROCESSING = "processing", "Processing"
        PAID = "paid", "Paid"
        FAILED = "failed", "Failed"
        CANCELLED = "cancelled", "Cancelled"

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name="sales")
    idempotency_key = models.CharField(max_length=100, unique=True,default=generate_idempotency_key(), editable=False)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.NEW)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)