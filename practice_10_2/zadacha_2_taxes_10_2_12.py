"""
ЗАДАЧА 2
Используя TDD методологию, напишите функцию сalculate_tax которая принимает два аргумента:
 - price - цена товара (float)
 - tax_rate - налоговый процент (float)
Функция должна вычислять стоимость товара с учётом налога и возвращать результат (float).
Требования:
 - Если price не положительная, функция должна возбуждать исключительную ситуацию ValueEError
   с сообщением "Неверная цена".
 - Если tax_rate меньше нуля или больше или равен 100 %, функция должна возбуждать
   исключительную ситуацию ValueError с сообщением "Неверный налоговый процент".

Пример использования:

result = calculate_tax(100, 10)
asset result == 110.0

result = calculate_tax(50, 5)
asset result == 52.5
"""


def calculate_tax(price: float, tax_rate: float) -> float:
    """вычисляет стоимость товара с учётом налога и возвращает результат"""
    if price < 0:
        raise ValueError("Неверная цена")
    if tax_rate < 0 or tax_rate >= 100:
        raise ValueError("Неверный налоговый процент")
    result = price * tax_rate / 100
    return result + price
