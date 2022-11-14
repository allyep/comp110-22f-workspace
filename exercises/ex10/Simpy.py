"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730389484"


class Simpy:
    """Designed to be able to work with numerical data at a higher level of abstraction."""
    values: list[float]

    def __init__(self, input: list[float]):
        """Initializes the values attribute of Simpy object to the argument."""
        self.values = input

    def __repr__(self) -> str:
        """Returns a string expressing Simpy with it's attribute values."""
        return f"Simpy({self.values})"

    def fill(self, fill_value: float, num_values: int) -> None:
        """Fills a Simpy's values with a specific number of repeating values."""
        i: int = 0 
        if len(self.values) != num_values:
            self.values = []
        while i < num_values:
            self.values.append(fill_value)
            i += 1
    
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fills the values attribute with range of values in terms of floats."""
        assert step != 0.0
        self.values.append(start)
        i: int = start 
        if i < 0:
            while i > stop - step:
                i += step
                self.values.append(i)
        while i < stop - step:
            i += step
            self.values.append(i)
        i = start

    def sum(self) -> float:
        """Returns the sum of all items in the values attribute."""
        Sum = sum(self.values)
        return Sum
    
    def __add__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Returns a new list that adds self and right hand side, either type Simpy or float."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for value in self.values:
                result.values.append(value + rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.values.append(self.values[i] + rhs.values[i])
        return result
    
    def __pow__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Returns a new list that raises self to the power of rhs, either type Simpy or float."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for value in self.values:
                result.values.append(value ** rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.values.append(self.values[i] ** rhs.values[i])
        return result
    
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Produces a mask based on the equality of each item in values attribute and with other Simpy or float value."""
        result: list[bool] = []
        equal: bool = False
        if isinstance(rhs, float):
            for value in self.values:
                if value == rhs:
                    equal = True 
                else:
                    equal = False
                result.append(equal)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                if self.values[i] == rhs.values[i]:
                    equal = True
                else: 
                    equal = False 
                result.append(equal)
        return result
    
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Produces a mask based on if self is greater than rhs."""
        result: list[bool] = []
        greater: bool = False
        if isinstance(rhs, float):
            for value in self.values:
                if value > rhs:
                    greater = True 
                else:
                    greater = False
                result.append(greater)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                if self.values[i] > rhs.values[i]:
                    greater = True
                else: 
                    greater = False 
                result.append(greater)
        return result
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Allow subscription notation."""
        if isinstance(rhs, int):
            result: float = self.values[rhs]
        else:
            assert len(self.values) == len(rhs)
            result: Simpy = Simpy([])
            for i in range(len(rhs)):
                if rhs[i] is True:
                    result.values.append(self.values[i])
        return result