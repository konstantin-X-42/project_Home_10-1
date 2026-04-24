"""
ЗАДАЧА 1
создайте проект, используя poetry, создайте структуру проекта и напишите
для функции calculate_taxes.
Отправьте код на GitHub.
Используйте фикстуры, параметризацию и добейтесь 100% code covarge.
"""


def calculate_taxes(prices: list[float], tax_rate: float) -> list[float]:
    """Функция вычисляет стоимость товаров с учётом налога."""
    if tax_rate < 0:
        raise ValueError("Неверный налоговый процент")
    taxed_prices = []
    for price in prices:
        if price <= 0:
            raise ValueError("Неверная цена")
        tax = price * tax_rate / 100
        taxed_prices.append(price + tax)
    return taxed_prices
