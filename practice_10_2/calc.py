def add(x: int | float, y: int | float) -> int | float:
    return x + y


def subtract(x: int | float, y: int | float) -> int | float:
    return x - y


def multiply(x: int | float, y: int | float) -> int | float:
    return x * y


def divide(x: int | float, y: int | float) -> int | float:
    if y == 0:
        raise ZeroDivisionError("Деление на ноль невозможно")
    return x / y
