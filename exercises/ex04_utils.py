"""EX04 - Use of 'list' utility functions."""

__author__ = "730389484"

def all(input: list[int], integer: int) -> bool:
    """Checks to see if integers in a list are all the same as given integer."""
    ind_check: int = 0 
    while ind_check < len(input):
        if input[ind_check] != integer:
            return False
        else:
            ind_check += 1
    return True
        

def max(input: list[int]) -> int:
    """Returns the maximum value in a given list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    max: int = input[0]
    index: int = 0
    while index < len(input):
        if input[index] > max:
            max = input[index]
        else: 
            index += 1                                                                                                                                                                                                                                                                                                                                                                                           
    return max
    
    
def is_equal(input_1: list[int], input_2: list[int]) -> bool:
    """Checks to see if every element at every index is equal in two give lists."""
    i: int = 0 
    while i < len(input_1) and i < len(input_2):
        if input_1[i] != input_2[i]:
            return False 
        else:
            i += 1
    return True 