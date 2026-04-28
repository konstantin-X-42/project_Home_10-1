# создаём тест для генератора
# функция бесконечный цикл
def infinite_sequence(start: int = 1):  # type: ignore
    while True:
        yield start
        start += 1


# пишем тест функции

# def test_infinite_sequence():
#     generator = infinite_sequence()
#     assert next(generator) == 1
#     assert next(generator) == 2
#     assert next(generator) == 3
#     # Дополнительные проверки
#     # по мере необходимости


# с видеоролика 11.1-9


def iterate(x0, m):  # type: ignore
    x = x0
    while True:
        yield x  # вместо print()
        x *= m


# for n in iterate(1, 1.2):
#     print(n)
#     if n > 3:
#         break


if __name__ == "__main__":
    # tests
    i = iterate(x0=1, m=1.2)  # type: ignore
    assert next(i) == 1
    assert next(i) == 1.2
    assert next(i) == 1.44
    assert next(i) == 1.728
