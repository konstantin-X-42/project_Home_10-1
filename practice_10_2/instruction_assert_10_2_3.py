def add_numbers(num1: int | float, num2: int | float) -> int | float:
    """Функция, складывающая два числа"""
    return num1 + num2


def is_even(num: int) -> bool:
    """Функция, проверяющая, является ли число четным"""
    if num % 2 == 0:
        return True
    else:
        return False


def find_max(numbers: list[int | float]) -> int | float:
    """Функция, находящая максимальное значение из списка чисел"""
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num


# ----------------------------------------------------- +


def add(x: int, y: int) -> int:
    return x + y


def subtract(x: int, y: int) -> int:
    return x - y


def multiply(x: int, y: int) -> int:
    return x * y


def divide(x: int, y: int) -> float:
    if y == 0:
        raise ZeroDivisionError("Деление на ноль невозможно")
    return x / y
