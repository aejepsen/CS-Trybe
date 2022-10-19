def my_sum(number1: int, number2: int) -> int:
    return number1 + number2


def test_sum_positive_number():
    assert my_sum(1, 3) == 5