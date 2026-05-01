# Внешняя функция принимает параметр x
def make_multiplier(x):  # type: ignore

    # Внутренняя функция использует значение x из внешней функции
    def multiplier(y):  # type: ignore
        return x * y

    # Возвращаем внутреннюю функцию
    return multiplier


if __name__ == "__main__":
    # Создаем замыкание
    double = make_multiplier(2)  # type: ignore
    print(double(5))
    # >>> 10
