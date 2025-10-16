from django.db import models
from uuid import uuid4

class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)