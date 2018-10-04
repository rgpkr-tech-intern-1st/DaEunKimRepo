import enum


class Name(enum.Enum):
    CASUAL = '분식'
    KOREAN = '한식'
    CHICKEN = '치킨'
    CHINESE = '중국집'
    JOKBAL = '족발보쌈'
    WESTERN = '피자양식'
    DESSERT = '카페디저트'
    JAPANESE = '일식돈까스'


class Id(enum.IntEnum):
    CASUAL = 1101
    KOREAN = 1102
    CHICKEN = 1103
    CHINESE = 1104
    JOKBAL = 1105
    WESTERN = 1106
    DESSERT = 1107
    JAPANESE = 1108
