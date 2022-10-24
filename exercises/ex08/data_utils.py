"""Dictionary related utility functions."""

__author__ = "730389484"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader: 
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result 


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result 


def head(column_table: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """Produce a new column-based table with only the first N rows of data for each column."""
    result: dict[str, list[str]] = {}
    i: int = 0 
    for column in column_table:
        N_values: list[str] = []
        if N >= len(column_table):
            result = column_table 
            return result
        while i < N:
            N_values.append(column_table[column][i])
            i += 1 
        result[column] = N_values 
        i = 0 
    return result


def select(table: dict[str, list[str]], selected_columns: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only selected columns that are needed."""
    result: dict[str, list[str]] = {}
    for column_name in selected_columns:
        result[column_name] = table[column_name]
    return result 


def concat(table_1: dict[str, list[str]], table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table with two column-based tables combined."""
    result: dict[str, list[str]] = {}
    for column in table_1:
        result[column] = table_1[column]
    for column in table_2:
        if column in result:
            result[column] += table_2[column]
        else: 
            result[column] = table_2[column]
    return result 


def count(values: list[str]) -> dict[str, int]:
    """Produces a dictionary displaying the frequency of unique values in a list."""
    result: dict[str, int] = {}
    for value in values:
        if value in result: 
            result[value] += 1
        else: 
            result[value] = 1
    return result