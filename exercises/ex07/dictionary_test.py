"""EX07 - Dictionary Testing."""

__author__ = "730389484"

from exercises.ex07.dictionary import invert, count, favorite_color


def test_invert_empty() -> None:
    """Tests that if given an empty dictionary, it returns an empty dictionary."""
    input: dict[str, str] = {}
    assert invert(input) == {}


def test_invert_one_pairing() -> None:
    """Tests if given dictionary with one pairing of key and value, returns one pairing that is inverted."""
    input: dict[str, str] = {'a': 'b'}
    assert invert(input) == {'b': 'a'}


def test_invert_same_pairing() -> None:
    """Tests if given dictionary with two of same key-value pairings, returns the same inverted key-value pairings."""
    input: dict[str, str] = {'ally': '10', 'ally': '10'}
    assert invert(input) == {'10': 'ally', '10': 'ally'}


def test_count_empty() -> None:
    """Tests empty dictionary is returned if given an empty list."""
    list_input: list[str] = []
    assert count(list_input) == {}


def test_count_all_same() -> None:
    """Tests if all of same values given, a dictionary with the count of only that value returned."""
    list_input: list[str] = ['2', '2', '2', '2', '2']
    assert count(list_input) == {'2': 5}


def test_count_one_of_each() -> None:
    """Tests that if there is only one of each item in list, dictionary will return the count for each item as 1."""
    list_input: list[str] = ['yes', 'no', 'maybe']
    assert count(list_input) == {'yes': 1, 'no': 1, 'maybe': 1}


def test_favorite_color_empty() -> None:
    """Tests that if given an empty dictonary, will not return any color."""
    names_and_colors: dict[str, str] = {}
    assert favorite_color(names_and_colors) == ""


def test_favorite_color_tie() -> None:
    """Tests that when there is a tie for color, the color appearing in dictionary first will return."""
    names_and_colors: dict[str, str] = {"Ally": "blue", "Kris": "green"}
    assert favorite_color(names_and_colors) == "blue"


def test_favorite_color_no_tie() -> None:
    """Tests that if given names and favorite colors in dictionary, the color appearing most frequently will return."""
    names_and_colors: dict[str, str] = {"Ally": "blue", "Kris": "blue", "Catherine": "pink"}
    assert favorite_color(names_and_colors) == "blue"