import random

"""
Библиотека random — содержит функции для генерации случайных чисел и выбора случайных элементов из списков.
"""
# --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --
print("\n--  --  1. Функция random() --  --  --\n")
# --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --

# import random

# random() — функция возвращает случайное число в диапазоне от 0 до 1 (не включая 1)
print(random.random())  # >>> 0.1381417864454676
print(random.random())  # >>> 0.08832548804303575
print(random.random())  # >>> 0.26012320315924387


# --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --
print("\n--  --  2. Функция randint(a, b) --  --  --\n")
# --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --

# import random

# randint(a, b) — функция возвращает случайное целое число в диапазоне от a до b (включая обе границы)
print(random.randint(1, 10))  # >>> 3
print(random.randint(1, 10))  # >>> 4
print(random.randint(1, 10))  # >>> 2


# --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --
print("\n--  --  3. Функция choice(seq) --  --  --\n")
# --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --

# import random

# choice(seq) — функция возвращает случайный элемент из последовательности seq
fruits = ["apple", "banana", "cherry"]
print(random.choice(fruits))  # >>> cherry
print(random.choice(fruits))  # >>> banana

print(random.choice("abcdef"))  # >>> e


# --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --
print("\n--  --  4. Функция shuffle(seq) --  --  --\n")
# --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --

# import random

# shuffle(seq) — функция перемешивает элементы последовательности seq.
cards = ["heart", "diamond", "club", "spade"]
random.shuffle(cards)
print(cards)  # ['diamond', 'spade', 'club', 'heart']

random.shuffle(cards)
print(cards)  # ['diamond', 'heart', 'club', 'spade']


# --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --
print("\n--  --  5. ЗАДАЧА --  --  --\n")
# --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --

"""
Задача
Напишите программу, которая симулирует игру в кости между двумя игроками.
Программа должна:
    - Бросить кости для каждого игрока (два шестигранных кубика для каждого игрока).
    - Сложить выпавшие значения для каждого игрока.
    - Объявить победителя, основываясь на сумме выпавших значений. Если суммы равны, объявить ничью.
"""
# import random


def throw_dice():  # type: ignore
    """2. функция симулирует одновременный бросок двух шестигранных кубиков и возвращает результаты"""
    return random.randint(1, 6), random.randint(1, 6)


# print(throw_dice())
# >>> (4, 6)


def play_game():  # type: ignore
    """1. Функция симулирует бросок костей двух игроков выводит очки и определяет победу"""
    player_1_dice_1, player_1_dice_2 = throw_dice()  # type: ignore
    sum_player_1 = player_1_dice_1 + player_1_dice_2
    print(f"Игрок 1 выбросил кости ({player_1_dice_1}, {player_1_dice_2}) на сумму {sum_player_1}")

    player_2_dice_1, player_2_dice_2 = throw_dice()  # type: ignore
    sum_player_2 = player_2_dice_1 + player_2_dice_2
    print(f"Игрок 2 выбросил кости ({player_2_dice_1}, {player_2_dice_2}) на сумму {sum_player_2}")

    if sum_player_1 > sum_player_2:
        print("Игрок 1 выиграл")
    elif sum_player_2 > sum_player_1:
        print("Игрок 2 выиграл")
    else:
        print("Ничья!")


# >>> Игрок 1 выбросил кости (1, 2) на сумму 3
# >>> Игрок 2 выбросил кости (3, 2) на сумму 5
# >>> Игрок 2 выиграл

if __name__ == "__main__":
    play_game()  # type: ignore
