from django.db import models


class Product(models.Model):

    id = models.CharField(
        primary_key=True,
        max_length=64
    )

    name = models.TextField()

    description = models.TextField(
        blank=True,
        null=True
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.id} - {self.name}"
