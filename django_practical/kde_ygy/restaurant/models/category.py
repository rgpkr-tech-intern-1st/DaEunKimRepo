from django.db import models

import enum


class Category(models.Model):
    class NameEnum(enum.Enum):
        CASUAL = '분식'
        KOREAN = '한식'
        CHICKEN = '치킨'
        CHINESE = '중국집'
        JOKBAL = '족발보쌈'
        WESTERN = '피자양식'
        DESSERT = '카페디저트'
        JAPANESE = '일식돈까스'

    class IdEnum(enum.IntEnum):
        CASUAL = 1101
        KOREAN = 1102
        CHICKEN = 1103
        CHINESE = 1104
        JOKBAL = 1105
        WESTERN = 1106
        DESSERT = 1107
        JAPANESE = 1108

    id = models.PositiveSmallIntegerField(
        primary_key=True,
        choices=[
            (id_enum.value, id_enum.value) for id_enum in IdEnum
        ],
    )
    name = models.CharField(
        max_length=10,
        null=False,
        choices=[
            (name_enum.value, name_enum.value) for name_enum in NameEnum
        ],
    )

    def __str__(self):
        return f'{self.name}-{self.id}'
