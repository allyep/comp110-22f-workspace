"""EX05 -- Using 'list' utility functions."""

__author__ = "730389484"


def only_evens(input: list[int]) -> list[int]:
    """Returns even numbers from list."""
    even_list: list[int] = list()
    i: int = 0
    for i in input:
        if i % 2 == 0:
            even_list.append(i)
        else:
            i += 1
    return even_list


def concat(input_1: list[int], input_2: list[int]) -> list[int]:
    """Returns a list containing all elements of the first list followed by all elements of the second list."""
    i: int = 0
    iteration: int = 0
    new_list: list[int] = []
    for i in input_1:
        new_list.append(i)
        i += 1
    for iteration in input_2:
        new_list.append(iteration)
        iteration += 1
    return new_list


def sub(a_list: list[int], start_ind: int, end_ind: int) -> list[int]:
    """Returns a list that is a subset of given list, between start index and end index - 1."""
    i: int = 0
    sub_list: list[int] = []
    if start_ind == len(a_list): 
        return sub_list
    if start_ind < 0:
        sub_list.append(a_list[0])
    if len(a_list) == 0 or start_ind > len(a_list) or end_ind <= 0:
        sub_list = []
        return sub_list
    while i < len(a_list):
        if i == start_ind:
            sub_list.append(a_list[i])
        i += 1
        if end_ind <= len(a_list) and i < end_ind and i > start_ind:
            sub_list.append(a_list[i])
    if end_ind > len(a_list):
        sub_list.append(a_list[len(a_list) - 1])
    return sub_list