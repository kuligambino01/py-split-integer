from app.split_integer import split_integer


def test_should_return_value_when_split_into_single_part() -> None:
    assert split_integer(1, 1) == [1]


def test_should_split_into_equal_parts_when_value_is_divisible_by_number_of_parts() -> None:
    assert split_integer(6, 2) == [3, 3]


def test_should_return_value_when_number_of_parts_is_one() -> None:
    assert split_integer(17, 1) == [17]


def test_should_return_sorted_parts_when_value_not_divisible_equally() -> None:
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


def test_should_handle_value_less_than_number_of_parts() -> None:
    assert split_integer(2, 3) == [0, 1, 1]