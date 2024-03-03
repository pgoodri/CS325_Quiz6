from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def get_area(self):
        # Abstract method to calculate the area of a shape
        raise NotImplementedError("Subclasses must implement get_area method.")


class Circle(Shape):
    def __init__(self, radius):
        # Initialize Circle object with radius
        self.radius = radius

    def get_area(self):
        # Calculate the area of the circle
        return pi * self.radius ** 2


class Square(Shape):
    def __init__(self, side_length):
        # Initialize Square object with side length
        self.side_length = side_length

    def get_area(self):
        # Calculate the are of the square 
        return self.side_length ** 2


class Rectangle(Shape):
    def __init__(self, length, width):
        # Initialize Rectangle object with length and width
        self.length = length
        self.width = width

    def get_area(self):
        # Calculate the area of the rectangle
        return self.length * self.width


def main():
    # Example usage
    circle = Circle(5)
    print("Area of circle:", circle.get_area())

    square = Square(4)
    print("Area of square:", square.get_area())

    rectangle = Rectangle(3, 6)
    print("Area of rectangle:", rectangle.get_area())


if __name__ == "__main__":
    main()