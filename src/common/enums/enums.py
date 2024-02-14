from enum import StrEnum, auto


class OrderStatus(StrEnum):
    in_progress = auto()
    complete = auto()
