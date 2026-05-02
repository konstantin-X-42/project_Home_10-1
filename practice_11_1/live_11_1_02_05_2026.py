# цикл работает только по итерируемым объектам: (str) (list) (dict) (tuple)
if __name__ == "__main__":

    str_data = "str"
    list_data = ["l", "i", "s", "t"]
    print("-- цикл for --")
    for data in list_data:
        print(data)

    # -------------------------------

    print("-- ИТЕРАТОР с iter() --")
    list_data = ["l", "i", "s", "t"]
    iter_object = iter(list_data)  # итерируемый объект: (list)
    print(type(iter_object))

    for item in iter_object:
        print(item)  # без функции next() итератор работает как обычный цикл

    # -------------------------------

    """итератор с iter() и next() ОБРАБОТКА ОШИБКИ StopIteration исключением Try и except"""
    # асинхронный код объект итератора используется для экономии ресурсов памяти, обработка
    # больших объёмов данных, для 100 элементов не актуален
    print("\n-- ИТЕРАТОР с iter() и next() и ловим ошибку --")
    list_data = ["l", "i", "s", "t"]
    iter_object = iter(list_data)
    print(next(iter_object))  # >>> l функция iter() вместе c функцией next() останавливают итератор сохраняя состояния
    print(next(iter_object))  # >>> i
    # ловим ошибку StopIteration по завершению итерации
    try:
        print(next(iter_object))  # >>> s
        print(next(iter_object))  # >>> t
        print(next(iter_object))  # >>> ошибка StopIteration - элементы в итераторе закончились
        print(next(iter_object))  # >>> ошибка StopIteration - элементы в итераторе закончились
    except StopIteration as e:
        print("Итерация завершена элементы закончились")

    # -------------------------------

    """итератор ОБРАБОТКА ОШИБКИ StopIteration циклом while()"""
    print("\n-- iter() и next() обрабатываем ошибку с помощью цикла while() --")
    list_data = ["l", "i", "s", "t"]  # обработка "бочеванием" библиотека itertools.batch есть метод batch
    # (методы с использованием итераторов ПОСМОТРЕТЬ)
    iter_object = iter(list_data)
    flag = True  # запускаем цикл
    while flag:
        try:
            print(next(iter_object))
        except StopIteration:
            flag = False  # обнаружена ошибка выключаем цикл
            print("Итерация завершена")

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
if __name__ == "__main__":
    """ГЕНЕРАТОР"""
    # если имеется yeld - это генератор
    # отличается от итератора присутствием дополнительного кода более расширенный функционал обработки
    print("\n-- ГЕНЕРАТОР тот же итератор --")
    """генератор в таком исполнении по функционалу тот же итератор"""

    def gen_example(lst_1: list):
        for item_1 in lst_1:
            yield item_1

    lst = [59, 120, 75, 1]
    gen_iter = gen_example(lst)  # запускаем генератор
    print(gen_iter)  # объект генератор - тот же итератор
    print(next(gen_iter))
    print(next(gen_iter))
    print(next(gen_iter))
    print(next(gen_iter))

    # -------------------------------

    print("\n-- ГЕНЕРАТОР обрабатывает по условию --")
    """генератор перебирает элементы и обрабатывает по условию"""

    def gen_example(lst: list):
        for item in lst:
            item = item / 100
            if item < 0.5:
                print("Было мало продаж")
            yield item

    lst = [59, 120, 75, 1]
    gen_iter = gen_example(lst)  # запускаем генератор
    print(gen_iter)  # объект генератор - тот же итератор
    print(next(gen_iter))
    # ловим ошибку StopIteration по завершению итерации
    try:
        print(next(gen_iter))  # >>> s
        print(next(gen_iter))  # >>> t
        print(next(gen_iter))  # >>> ошибка StopIteration - элементы в итераторе закончились
        print(next(gen_iter))  # >>> ошибка StopIteration - элементы в итераторе закончились
    except StopIteration as e:
        print("Итерация завершена элементы закончились")
