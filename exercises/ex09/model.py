"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi
from math import sqrt


__author__ = "730389484"  


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)

    def distance(self, other_cell: Point) -> int:
        """Determine distance between two points."""
        distance: int = sqrt((self.x - other_cell.x)**2 + (self.y - other_cell.y)**2)
        return distance


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    def tick(self) -> None: 
        """Reassign the object's location attribute with the result of adding the self object's location with its direction."""
        self.location = self.location.add(self.direction)
        if self.is_infected():
            self.sickness += 1
            if self.sickness > constants.RECOVERY_PERIOD:
                self.immunize()
    
    def contract_disease(self) -> None:
        """Assigns INFECTED to the sickness attribute of the cell object the method is called on."""
        self.sickness = constants.INFECTED
    
    def is_vulnerable(self) -> None:
        """Returns True when the cell's sickness attribute is equal to VULNERABLE and False otherwise."""
        if self.sickness == constants.VULNERABLE:
            return True
        else: 
            return False
    
    def is_infected(self) -> None:
        """Returns truth value of cell being infected."""
        if self.sickness >= constants.INFECTED:
            return True
        else:
            return False 

    def color(self) -> str:
        """Changes color of cell to represent if a cell is vulnerable, infected, or immune."""
        if self.is_vulnerable():
            return "gray"
        elif self.is_infected():
            return "blue"
        elif self.is_immune():
            return "green"
    
    def contact_with(self, other_cell: Cell) -> None:
        """Infects other cell if infected cell makes contact with it."""
        if self.is_infected() and other_cell.is_vulnerable():
            other_cell.contract_disease()
        if other_cell.is_infected() and self.is_vulnerable():
            self.contract_disease()
        else:
            self.is_immune()

    def immunize(self) -> None:
        """Assigns immunity to the sickness attribute of the object that the method is called on."""
        self.sickness = constants.IMMUNE

    def is_immune(self) -> None:
        """Returns truth value of sell being immune."""
        if self.sickness == constants.IMMUNE:
            return True 
        else:
            return False


class Model:   
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, num_infected: int, num_immune: int = 0):
        """Initialize the cells with random locations and directions, as well as infection."""
        self.population = []
        for _ in range(cells):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            self.population.append(cell)
        if num_infected + num_immune >= cells:
            raise ValueError("The total number of cells that start as immune or infected must not exceed the amount of cells in the population.")
        if num_infected >= cells or num_infected <= 0:
            raise ValueError("There must be cells that start as infected and total to be less than the total in the population.")
        for i in range(num_infected):
            self.population[i].contract_disease()
        if num_immune > cells or num_immune < 0:
            raise ValueError("There must exist cells that start as immune and total to be less than the total in the population.")  
        imm_cell: int = 0 
        i: int = 0
        while i < len(self.population):
            j: int = i + 1
            while j > num_infected and imm_cell < num_immune:
                self.population[j].immunize()
                j += 1
                imm_cell += 1
            i += 1

    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()
        
    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0
        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0
        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1.0
        if cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1.0
            
    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        for cell in self.population:
            if cell.is_infected():
                return False
        return True

    def check_contacts(self) -> None:
        """Checks for contact between every pair of cells."""
        i: int = 0 
        while i < len(self.population):
            j: int = i + 1
            while j < len(self.population):
                if self.population[i].location.distance(self.population[j].location) < constants.CELL_RADIUS:
                    self.population[i].contact_with(self.population[j]) 
                j += 1
            i += 1