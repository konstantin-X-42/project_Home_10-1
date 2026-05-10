import datetime
from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    Декоратор для логирования работы функций.
    :param filename: Путь к файлу лога. Если None, вывод только в консоль.
    """

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args, **kwargs):
            now = datetime.datetime.now().strftime("%Y.%m.%d %H:%M:%S.%f")[
                :-3
            ]  # фиксирует время обращения к декоратору в формате Г.М.Д Ч:М:С:млС
            try:
                result = func(*args, **kwargs)
                log_message = (
                    f"{now} {func.__name__} успешно\n"  # сообщение в лог, now - дата и время, название функции
                )

                _write_log(log_message, filename)  # функция внутренняя записывает текст log_message в адрес filename
                return result

            except Exception as e:  # Если произошла ошибка фиксируем в лог
                log_message = (
                    f"{now} {func.__name__} error: {type(e).__name__}. "  # дата,время,тип ошибки
                    f"Inputs: {args}, {kwargs}\n"  # и входные аргументы
                )
                _write_log(log_message, filename)  # записываем в лог
                raise e  # Пробрасываем ошибку дальше

        return wrapper

    return decorator


def _write_log(message, filename):
    """Вспомогательная функция для вывода лога"""
    if filename:
        with open(
            filename, "a", encoding="utf-8"
        ) as f:  # открой файл, приготовься к записи данных "a" - в самый конец
            f.write(message)  # запись текста в файл
    else:
        print(message.strip())  # вывод сообщения на экран
