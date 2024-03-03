from abc import ABC, abstractmethod


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
        return 3.14 * self.radius ** 2

    def set_radius(self, radius):
        # Set the radius of the circle
        self.radius = radius


class Rectangle(Shape):
    def __init__(self, length, width):
        # Initialize Rectangle object with length and width
        self.length = length
        self.width = width

    def get_area(self):
        # Calculate the area of the rectangle
        return self.length * self.width

    def set_width(self, width):
        # Set the width of the rectangle
        self.width = width

    def set_height(self, height):
        # Set the height of the rectangle
        self.length = height


class Triangle(Shape):
    def __init__(self, base, height):
        # Initialize Triangle object with base and height
        self.base = base
        self.height = height

    def get_area(self):
        # Calculate the area of the trianlge
        return 0.5 * self.base * self.height


class Polygon(Shape):
    def __init__(self, sides, side_length):
        # Initialize Polygon object with number of sides and side length
        self.sides = sides
        self.side_length = side_length

    def get_area(self):
        # Implement area calculation for polygon
        return 0


def main():
    # Example usage
    circle = Circle(5)
    print("Area of circle:", circle.get_area())

    rectangle = Rectangle(3, 6)
    print("Area of rectangle:", rectangle.get_area())

    triangle = Triangle(4, 5)
    print("Area of triangle:", triangle.get_area())


if __name__ == "__main__":
    main()