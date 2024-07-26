# Lab 7
# Replace "WRITE CODE HERE" with your python code and remove the "pass" statement


# ----------------- Question 1 -----------------


class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"

class Bike(Vehicle):
    def __init__(self, make, model, year, bike_type):
        super().__init__(make, model, year)
        self.bike_type = bike_type

    def __str__(self):
        return f"{super().__str__()}, {self.bike_type} type"

class Car(Vehicle):
    miles_per_battery_percent = 4
    miles_per_gallon = 30

    def __init__(self, make, model, year, is_electric=False):
        super().__init__(make, model, year)
        self.is_electric = is_electric

    def __str__(self):
        return f"{super().__str__()}, {'Electric' if self.is_electric else 'Non-Electric'}"

    def driving_range(self, energy):
        if self.is_electric:
            return self.miles_per_battery_percent * energy
        else:
            return self.miles_per_gallon * energy

# Example usage
my_car = Car("Tesla", "Model S", 2020, is_electric=True)
print(my_car)  # Expected output: "2020 Tesla Model S, Electric"

my_non_electric_car = Car("Ford", "Mustang", 1965, is_electric=False)
print(my_non_electric_car)  # Expected output: "1965 Ford Mustang, Non-Electric"

# Demonstrating the driving range method
print("Electric Car Driving Range:", my_car.driving_range(50))  # Expected output: “Electric Car Driving Range: 200”
print("Non-Electric Car Driving Range:", my_non_electric_car.driving_range(10))  # Expected output: “Non-Electric Car Driving Range: 300”

my_bike = Bike("Trek", "Domane", 2019, "road")
print(my_bike)  # Expected output: "2019 Trek Domane, road type"




# ----------------- Question 2 -----------------


class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        real_part = self.real * other.real - self.imaginary * other.imaginary
        imaginary_part = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(real_part, imaginary_part)

    def __str__(self):
        return f"ComplexNumber with real part {self.real} and imaginary part {self.imaginary}"

a = ComplexNumber(2, 3)
b = ComplexNumber(1, 7)
c = a + b
d = a * b

print(c)
print(d)


# invoke the function with relevant args of your choice
# WRITE CODE HERE


# ----------------- Question 3 -----------------
from math import pi

class Shape:
    def area(self):
        raise NotImplementedError("This method should be overridden by subclasses")
    
    def dimensions(self):
        raise NotImplementedError("This method should be overridden by subclasses")

class Rectangle(Shape):
    def __init__(self, **kwargs):
        if 'side' in kwargs:
            self.length = self.width = kwargs['side']
        else:
            self.length = kwargs.get('length', 0)
            self.width = kwargs.get('width', 0)

    def area(self):
        return self.length * self.width

    def dimensions(self):
        if self.length == self.width:
            return {'side': self.length}
        else:
            return {'length': self.length, 'width': self.width}

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(pi * self.radius ** 2, 2)  # Round the area to two decimal places

    def dimensions(self):
        return {'radius': self.radius}

# Example usage
rectangle = Rectangle(length=5, width=10)
print(rectangle.area())
print(rectangle.dimensions())

square = Rectangle(side=5)
print(square.area())
print(square.dimensions())

circle = Circle(radius=7)
print(circle.area())  # Now the output will match the expected values in the tests
print(circle.dimensions())
