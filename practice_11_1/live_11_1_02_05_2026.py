import pytest

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
    except StopIteration:
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
    print("\n-- ГЕНЕРАТОР в таком исполнении по функционалу тот же итератор --")

    def gen_example(lst_p1: list):  # type: ignore
        for item_1 in lst_p1:
            yield item_1

    lst = [59, 120, 75, 1]
    gen_iter = gen_example(lst)  # запускаем генератор
    print(gen_iter)  # объект генератор - тот же итератор
    print(next(gen_iter))
    print(next(gen_iter))
    print(next(gen_iter))
    print(next(gen_iter))

    # -------------------------------

    print("\n-- ГЕНЕРАТОР перебирает элементы и обрабатывает по условию, исключена ошибка --")

    def gen_example(lst_r: list):  # type: ignore
        for item_ in lst_r:
            item_ = item_ / 100
            if item_ < 0.5:
                print("Было мало продаж")
            yield item_

    lst = [59, 120, 75, 1]  # задаём параметры
    gen_iter = gen_example(lst)  # запускаем генератор
    print(gen_iter)  # объект генератор - тот же итератор

    try:
        print(next(gen_iter))  # >>> 0.59
        print(next(gen_iter))  # >>> 1.2
        print(next(gen_iter))  # >>> 0.75
        print(next(gen_iter))  # >>> исключение ошибки StopIteration - Итерация завершена
        print(next(gen_iter))  # >>> ошибка StopIteration - элементы в итераторе закончились
    except StopIteration:  # ловим ошибку StopIteration - завершение итерации
        print("Итерация завершена элементы закончились")

    # -------------------------------

    print("\n-- ГЕНЕРАТОР поочерёдно выводит list_1 и list_2 обработка ошибки --")

    def gen_chain(list_r1: list, list_r2: list):  # type: ignore # функция MapReduce
        for i in range(len(list_1)):
            yield list_r1[i]  # 1 # 3 состояние
            print("код на исполнение на чётном вызове 2, 4, 6 и тд")  # 2 # 4 исполнение
            yield list_r2[i]  # 2 # 4 состояние

    list_1 = [59, 120, 75, 1]  # задаём параметры
    list_2 = ["l", "i", "s", "t"]  # задаём параметры

    gen_iter = gen_chain(list_1, list_2)
    print(next(gen_iter))  # <<< 59  с списка list_1
    print(next(gen_iter))  # <<< l   с списка list_2
    print(next(gen_iter))  # <<< 120 с списка list_1
    print(next(gen_iter))  # <<< i   с списка list_2

    flag = True  # запускаем цикл
    while flag:
        try:
            print(next(gen_iter))
        except StopIteration:
            flag = False  # обнаружена ошибка выключаем цикл
            print("Итерация завершена")

    # -------------------------------

    print("\n-- ГЕНЕРАТОР одновременно выводит lst_1 и lst_2 в картеж, затем 123 --")

    def gen_chain(lst_s1: list, lst_s2: list):  # type: ignore
        for i in range(len(lst_s1)):
            yield lst_s1[i], lst_s2[i]  # 1, 3
            print("Окно между yield")
            yield 123  # 2, 4

    lst_1 = [59, 120, 75, 1]
    lst_2 = ["l", "i", "s", "t"]

    gen_iter = gen_chain(lst_1, lst_2)
    print(next(gen_iter))
    print(next(gen_iter))
    print(next(gen_iter))
    print(next(gen_iter))

    # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

    print("\n-- ГЕНЕРАТОР ТЕСТЫ assert --")

    def gen_chain(lst_s1: list, lst_s2: list):  # type: ignore
        for i in range(len(lst_s1)):
            yield lst_s1[i]  # 1, 3
            # print("Окно между yield")
            yield lst_s2[i]  # 2, 4

    list_1 = [59, 120, 75, 1]  # задаём параметры
    list_2 = ["l", "i", "s", "t"]  # задаём параметры

    gen_iter = gen_chain(list_1, list_2)
    print(list(gen_iter))  # <<< выдаёт все элементы генератора

    gen_iter = gen_chain(lst_1, lst_2)  # генератор опустошён, если для
    # теста необходимо проверить элементы, вызываем генератор повторно
    print(next(gen_iter))  # <<< 59
    print(next(gen_iter))  # <<< l
    print(next(gen_iter))  # <<< 120

    def test_gen_chain():  # type: ignore
        lst_t1 = [59, 120]
        lst_t2 = ["l", "i"]
        gen_iter_1 = gen_chain(lst_t1, lst_t2)  # <<< вызываем генератор

        result_lst_g = [59, "l", 120, "i"]
        assert list(gen_iter_1) == result_lst_g

        gen_iter_2g = gen_chain(lst_t1, lst_t2)  # <<< вызываем генератор
        assert next(gen_iter_2g) == result_lst_g[0]
        assert next(gen_iter_2g) == result_lst_g[1]
        assert next(gen_iter_2g) == result_lst_g[2]
        assert next(gen_iter_2g) == result_lst_g[3]

    test_gen_chain()  # type: ignore

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

print("\n-- ГЕНЕРАТОР ТЕСТЫ parametrize --")


def gen_chain(lst_s1: list, lst_s2: list):  # type: ignore
    for i in range(len(lst_s1)):
        yield lst_s1[i]  # 1, 3
        # print("Окно между yield")
        yield lst_s2[i]  # 2, 4


@pytest.mark.parametrize(  # type: ignore
    "lst_x1, lst_x2, result_lst_x",
    [
        ([59, 120], ["l", "i"], [59, "l", 120, "i"]),
        ([590, 1200], ["ll", "ii"], [590, "ll", 1200, "ii"]),
    ],
)
def test_gen_chain(lst_x1, lst_x2, result_lst_x):  # type: ignore
    gen_iter_ = gen_chain(lst_x1, lst_x2)
    assert list(gen_iter_) == result_lst_x


"""блок ниже даёт возможность запустить через shift + fn + F10 в консоль"""
if __name__ == "__main__":
    import pytest

    pytest.main([__file__])

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

print("\n-- ИТЕРАТОР ТЕСТЫ asert --")


def gen_iter():  # type: ignore
    user_input = "list"  # input("какая то строка") укажем пользователь ввел list
    iter_object_ = iter(user_input)
    return next(iter_object_)


def test_gen_chain_iterator():  # type: ignore
    lis_data = ["l", "i", "s", "t"]
    iter_object_ = iter(lis_data)

    assert list(iter_object_) == lis_data

    iter_object_ = iter(lis_data)
    assert next(iter_object_) == lis_data[0]
    assert next(iter_object_) == lis_data[1]
    assert next(iter_object_) == lis_data[2]
    assert next(iter_object_) == lis_data[3]


# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

print("\n-- ИТЕРАТОР ТЕСТЫ asert и тест ошибки StopIteration --")

list_x1 = [59, 120, 75, 1]  # задаём параметры
list_x2 = ["l", "i", "s", "t"]  # задаём параметры

gen_iter_2 = gen_chain(list_x1, list_x2)
print(list(gen_iter_2))  # функция list вырабатывает все элементы в итераторе


def test_gen_chain():  # type: ignore
    lst_x1 = [62, 530]  # объявляем элементы для теста в списке 1 (элементы могут быть иные)
    lst_x2 = ["g", "i"]  # объявляем элементы для теста в списке 2 (элементы могут быть иные)
    gen_iter_x = gen_chain(lst_x1, lst_x2)  # запускаем итератор

    result_gen = [62, "g", 530, "i"]  # объявляем результат итератора для теста
    assert list(gen_iter_x) == result_gen  # запускаем тест на весь список объединяющий два списка, опустошаем итератор

    gen_iter_x = gen_chain(lst_x1, lst_x2)  # запускаем итератор вновь, предыдущий исчерпан
    assert next(gen_iter_x) == result_gen[0]  # элементы с 0-м индексом в двух списках сравниваем с результатом
    assert next(gen_iter_x) == result_gen[1]
    assert next(gen_iter_x) == result_gen[2]
    assert next(gen_iter_x) == result_gen[3]
    with pytest.raises(StopIteration):
        assert next(gen_iter_x) == result_lst[3]


test_gen_chain()  # type: ignore

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

print("\n-- ИТЕРАТОР ТЕСТЫ asert и тест ошибки AssertionError --")

lst_1 = [59, 120]
lst_2 = ["l", "i"]
gen_iter_v = gen_chain(lst_1, lst_2)

result_lst = [59, "l", 120, "i"]
assert list(gen_iter_v) == result_lst

gen_iter_v = gen_chain(lst_1, lst_2)
with pytest.raises(AssertionError):  # AssertionError - утверждение в коде не совпадает с реальностью
    assert next(gen_iter_v) == result_lst[1]  # 59 == l -проверяем ошибку AssertionError

test_gen_chain()  # type: ignore

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

"""разделение на группы значимости по обработке ошибок"""


def print_info():  # type: ignore
    try:
        print("Поведение")
    except KeyError:  # отлавливаем определённую ошибку внутри функции
        pass  # обработка ошибки не требующей внимания


try:
    print_info()  # type: ignore
except Exception:  # отлавливаем внешнюю ошибку или определенные ошибки функции
    pass  # обработка критичной ошибки требующая оперативности разработчика

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

print("\n-- Списковое включение с условием else --")

lst = [1, 2, 3, 4, 5]  # список занимает память
list_data = [x if x % 2 == 0 and x > 3 else 0 for x in lst]  # type: ignore # список занимает память
print(list_data)  # список

# -------------------------------

print("\n-- аналогия в одну строку --")
new_lst = []
for x in lst:
    if x % 2 == 0:
        new_lst.append(lst)
    else:
        "0"
print(list_data)

# -------------------------------

print("\n-- однострочный генератор списка с условием else --")
lst = [1, 2, 3, 4, 5]  # список занимает память
gen_data = (x if x % 2 == 0 and x > 3 else 0 for x in lst)  # хранит только состояние
print(gen_data)  # генератор
print(next(gen_data))  # перебираем каждый элемент генератора через функцию next()
print(next(gen_data))
print(next(gen_data))
print(next(gen_data))
print(next(gen_data))

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

print("\n-- база для асинхронного программирования передаётся управление yield from --")


def gen_data(lst_y1):  # type: ignore
    for item_y in lst_y1:
        yield item_y
        print("Окно между yield")
        yield from [100, 200, 300]  # from передаёт управление, хранит состояния до выработки списка


lst_yy1 = [1, 2, 3, 4, 5]
gen_iter_y = gen_data(lst_yy1)  # type: ignore
print(next(gen_iter_y))  # >>> 1    из списка lst_yy1
print(next(gen_iter_y))  # >>> 100  из списка yield from
print(next(gen_iter_y))  # >>> 200  из списка yield from
print(next(gen_iter_y))  # >>> 300  из списка yield from
print(next(gen_iter_y))  # >>> 2    из списка lst_yy1
print(next(gen_iter_y))  # >>> 100  из списка yield from
print(next(gen_iter_y))  # >>> 200  из списка yield from
