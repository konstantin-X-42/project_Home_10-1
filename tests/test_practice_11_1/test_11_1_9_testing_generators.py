from practice_11_1.x11_1_9_testing_generators import infinite_sequence

def test_infinite_sequence():
    generator = infinite_sequence()
    assert next(generator) == 1
    assert next(generator) == 2
    assert next(generator) == 3
    # Дополнительные проверки
    # по мере необходимости