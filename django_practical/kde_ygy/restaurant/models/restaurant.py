from django.db import models

from datetime import time

from .category import Category


class Restaurant(models.Model):
    category = models.ManyToManyField(
        Category,
        null=False,
    )
    id = models.BigAutoField(
        primary_key=True,
    )
    is_franchise = models.BooleanField(
        default=False,
    )
    name = models.CharField(
        max_length=20,
        null=False,
        default='미기입',
        unique=True,
    )
    address = models.CharField(
        max_length=40,
        null=False,
        default='미기입',
    )
    postal_code = models.CharField(
        max_length=10,
        null=False,
    )
    minimum_order_price = models.PositiveSmallIntegerField(
        null=False,
    )
    open_time = models.TimeField(
        auto_now=False,
        auto_now_add=False,
        default=time.min,
    )
    close_time = models.TimeField(
        auto_now=False,
        auto_now_add=False,
        default=time.max,
    )

    class Meta:
        verbose_name = 'Restaurant'
        verbose_name_plural = 'Restaurants'

    def __str__(self):
        return f'{self.name}({self.category}) - 최소주문금액 {self.minimum_order_price}'
