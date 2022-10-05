"""EX05 -- Unit Tests."""

__author__ = "730389484"

from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_empty() -> None:
    """Test that if given an empty list, it returns an empty list."""
    input: list[int] = []
    assert only_evens(input) == []


def test_only_evens_even() -> None: 
    """Tests that if given even value, returns, even value."""
    input: list[int] = [2]
    assert only_evens(input) == [2]


def test_only_evens_even_and_odd() -> None:
    """Tests that if given even and odd values in list, only returns list with even values."""
    input: list[int] = [1, 2, 3, 4]
    assert only_evens(input) == [2, 4]


def test_concat_empty() -> None:
    """Tests that if given two empty lists, will return an empty list."""
    input_1: list[int] = []
    input_2: list[int] = []
    assert concat(input_1, input_2) == []


def test_concat_diff_lengths() -> None:
    """Tests that if given different length lists, still returns the first followed by the second."""
    input_1: list[int] = [1, 2]
    input_2: list[int] = [3, 4, 5]
    assert concat(input_1, input_2) == [1, 2, 3, 4, 5]


def test_concat_same_lists() -> None:
    """Tests that if given two identical lists, still returns the first followed by second."""
    input_1: list[int] = [6, 4, 7]
    input_2: list[int] = [6, 4, 7]
    assert concat(input_1, input_2) == [6, 4, 7, 6, 4, 7]


def test_sub_start_equals_length() -> None:
    """Tests that if start index equals length of list, will return an empty list."""
    a_list: list[int] = [1, 2]
    start_ind: int = 2
    end_ind: int = 3
    assert sub(a_list, start_ind, end_ind) == []


def test_sub_indexes_in_list() -> None:
    """Tests that if both indexes are within the length of the list, will return the sub-list including start index until end index (noninclusive)."""
    a_list: list[int] = [1, 2, 3, 4]
    start_ind: int = 1
    end_ind: int = 3
    assert sub(a_list, start_ind, end_ind) == [2, 3]


def test_sub_only_first_index() -> None:
    """Tests that if start index is 0 and end index is 1, only the value at first index of list will return."""
    a_list: list[int] = [2, 4, 6, 8, 10, 12, 14]
    start_ind: int = 0
    end_ind: int = 1
    assert sub(a_list, start_ind, end_ind) == [2]