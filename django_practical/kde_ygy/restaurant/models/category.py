from django.db import models

from ..enums.category_choice import Id, Name


class Category(models.Model):
    id = models.PositiveSmallIntegerField(
        primary_key=True,
        default=0,
        choices=[
            (c_id.value, c_id.value) for c_id in Id
        ],
    )
    name = models.CharField(
        max_length=10,
        null=False,
        choices=[
            (c_name.value, c_name.value) for c_name in Name
        ],
    )


