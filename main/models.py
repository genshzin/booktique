import uuid
from django.db import models

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    stock_quantity = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.name