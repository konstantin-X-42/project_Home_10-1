"""
Создайте проект, используя poetry, создайте структуру проекта и напишите тесты для функции
calculate_taxes
Отправьте код на GitHub.
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


if __name__ == "__main__":
    my_price = [10.0, 20.0, 30.0]
    my_tax = 10
    result = calculate_taxes(my_price, my_tax)
    print(result)
# ********1***********
# запускаем выводит: >>> [11.0, 22.0, 33.0]
# *******************
