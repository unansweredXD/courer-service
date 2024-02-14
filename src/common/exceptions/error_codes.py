from enum import Enum


class ErrorCodes(Enum):
    """
    Ошибка в формате: имя = (код, HTTP код, описание)
    """

    not_allow = (0, 403, "нет доступа")
    not_found = (0, 404, "страница не найдена")
