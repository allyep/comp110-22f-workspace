"""EX07 - Dictionaries."""

__author__ = "730389484"

def invert(input: dict[str, str]) -> dict[str, str]:
    """Returns a dictionary with inverted keys and values."""
    invert_result: dict[str, str] = {}   
    for key in input:
        if input[key] not in invert_result:
            invert_result[input[key]] = key
        else:
            raise KeyError("There is a duplicate key.")
    return invert_result


def favorite_color(names_and_colors: dict[str, str]) -> str:
    """Returns the color that appears most frequently in the dictionary."""
    most_frequent_color: str = ""
    frequency_dict: dict[str, int] = {}
    counter: int = 0
    for name in names_and_colors:
        if names_and_colors[name] in frequency_dict:
            frequency_dict[names_and_colors[name]] += 1
        else: 
             frequency_dict[names_and_colors[name]] = 1
        if frequency_dict[names_and_colors[name]] > counter:
            counter = frequency_dict[names_and_colors[name]]
            most_frequent_color = names_and_colors[name] 
    return most_frequent_color

    

def count(list_input: list[str]) -> dict[str, int]:
    """Produces dictionary with values as the count of number of times a value appeared in a list."""
    counts_dict: dict[str, int] = {}
    for value in list_input:
        if value in counts_dict:
            counts_dict[value] += 1
        else:
            counts_dict[value] = 1
    return counts_dict
