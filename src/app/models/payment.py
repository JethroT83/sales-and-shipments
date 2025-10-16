from django.db import models
from uuid import uuid4
from .sale import Sale

class Payment(models.Model):
    class Status(models.TextChoices):
        AUTHORIZED = "authorized", "Authorized"
        CAPTURED  = "captured", "Captured"
        FAILED    = "failed", "Failed"

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    sale = models.OneToOneField(Sale, on_delete=models.CASCADE, related_name="payment")
    provider = models.CharField(max_length=50)       # e.g., stripe
    provider_ref = models.CharField(max_length=100)  # charge id
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=Status.choices)
    created_at = models.DateTimeField(auto_now_add=True)