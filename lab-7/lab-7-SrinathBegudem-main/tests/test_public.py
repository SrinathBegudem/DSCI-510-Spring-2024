import random
import pytest

from lab_7 import Vehicle, Car, Bike
from lab_7 import ComplexNumber
from lab_7 import Shape, Rectangle, Circle


@pytest.mark.timeout(0.3)
def test_vehicle_parent():
    veh = Vehicle("Manufacturer", "Model", 2020)
    assert veh.make == "Manufacturer"
    assert veh.model == "Model"
    assert veh.year == 2020
    assert str(veh) == "2020 Manufacturer Model"


@pytest.mark.timeout(0.3)
def test_vehicle_child_car_electric():
    car = Car("Tesla", "Model S", 2020, is_electric=True)
    assert str(car) == "2020 Tesla Model S, Electric"
    assert car.driving_range(50) == 200


@pytest.mark.timeout(0.3)
def test_vehicle_child_car_gas():
    car = Car("Ford", "Mustang", 2019, is_electric=False)
    assert str(car) == "2019 Ford Mustang, Non-Electric"
    assert car.driving_range(50) == 1500


@pytest.mark.timeout(0.3)
def test_vehicle_child_bike_mountain():
    bike = Bike("Trek", "Domane", 2018, "mountain")
    assert str(bike) == "2018 Trek Domane, mountain type"
    assert bike.bike_type == "mountain"


@pytest.mark.timeout(0.3)
def test_vehicle_child_bike_road():
    bike = Bike("Harley Davidson", "Fat Boy", 2012, "road")
    assert str(bike) == "2012 Harley Davidson Fat Boy, road type"
    assert bike.bike_type == "road"


@pytest.mark.timeout(0.3)
def test_complex_number_1():
    cn_1 = ComplexNumber(2, 3)
    cn_2 = ComplexNumber(1, 7)

    assert str(cn_1) == "ComplexNumber with real part 2 and imaginary part 3"
    assert str(cn_2) == "ComplexNumber with real part 1 and imaginary part 7"

    cn_add = cn_1 + cn_2
    cn_mul = cn_1 * cn_2

    assert str(cn_add) == "ComplexNumber with real part 3 and imaginary part 10"
    assert isinstance(cn_add, ComplexNumber)
    assert str(cn_mul) == "ComplexNumber with real part -19 and imaginary part 17"
    assert isinstance(cn_mul, ComplexNumber)


@pytest.mark.timeout(0.3)
def test_complex_number_2():
    cn_1 = ComplexNumber(100, -3)
    cn_2 = ComplexNumber(99, 1)

    assert str(cn_1) == "ComplexNumber with real part 100 and imaginary part -3"
    assert str(cn_2) == "ComplexNumber with real part 99 and imaginary part 1"

    cn_add = cn_1 + cn_2
    cn_mul = cn_1 * cn_2

    assert str(cn_add) == "ComplexNumber with real part 199 and imaginary part -2"
    assert isinstance(cn_add, ComplexNumber)
    assert str(cn_mul) == "ComplexNumber with real part 9903 and imaginary part -197"
    assert isinstance(cn_mul, ComplexNumber)


@pytest.mark.timeout(0.3)
def test_complex_number_3():
    cn_1 = ComplexNumber(0, 3)
    cn_2 = ComplexNumber(1, -7)

    assert str(cn_1) == "ComplexNumber with real part 0 and imaginary part 3"
    assert str(cn_2) == "ComplexNumber with real part 1 and imaginary part -7"

    cn_add = cn_1 + cn_2
    cn_mul = cn_1 * cn_2

    assert str(cn_add) == "ComplexNumber with real part 1 and imaginary part -4"
    assert isinstance(cn_add, ComplexNumber)
    assert str(cn_mul) == "ComplexNumber with real part 21 and imaginary part 3"
    assert isinstance(cn_mul, ComplexNumber)


@pytest.mark.timeout(0.3)
def test_complex_number_4():
    cn_1 = ComplexNumber(-2, -3)
    cn_2 = ComplexNumber(-1, -7)

    assert str(cn_1) == "ComplexNumber with real part -2 and imaginary part -3"
    assert str(cn_2) == "ComplexNumber with real part -1 and imaginary part -7"

    cn_add = cn_1 + cn_2
    cn_mul = cn_1 * cn_2

    assert cn_add.real == -3
    assert cn_add.imaginary == -10
    assert isinstance(cn_add, ComplexNumber)
    assert cn_mul.real == -19
    assert cn_mul.imaginary == 17
    assert isinstance(cn_mul, ComplexNumber)


@pytest.mark.timeout(0.3)
def test_complex_number_5():
    cn_1 = ComplexNumber(0, 1)
    cn_2 = ComplexNumber(0, -1)

    assert str(cn_1) == "ComplexNumber with real part 0 and imaginary part 1"
    assert str(cn_2) == "ComplexNumber with real part 0 and imaginary part -1"

    cn_add = cn_1 + cn_2
    cn_mul = cn_1 * cn_2

    assert cn_add.real == 0
    assert cn_add.imaginary == 0
    assert isinstance(cn_add, ComplexNumber)

    assert cn_mul.real == 1
    assert cn_mul.imaginary == 0
    assert isinstance(cn_mul, ComplexNumber)


@pytest.mark.timeout(0.3)
def test_shape_parent():
    s = Shape()
    assert isinstance(s, Shape)
    with pytest.raises(
        NotImplementedError, match="This method should be overridden by subclasses"
    ):
        s.area()

    with pytest.raises(
        NotImplementedError, match="This method should be overridden by subclasses"
    ):
        s.dimensions()


@pytest.mark.timeout(0.3)
def test_shape_rectangle():
    r = Rectangle(length=10, width=50)
    assert isinstance(r, Rectangle)
    assert r.area() == 500
    assert r.dimensions() == {"length": 10, "width": 50}


@pytest.mark.timeout(0.3)
def test_shape_square():
    r = Rectangle(side=10)
    assert isinstance(r, Rectangle)
    assert r.area() == 100
    assert r.dimensions() == {"side": 10}


@pytest.mark.timeout(0.3)
def test_shape_circle_1():
    r = Circle(radius=5)
    assert isinstance(r, Circle)
    assert r.area() == 78.54
    assert r.dimensions() == {"radius": 5}


@pytest.mark.timeout(0.3)
def test_shape_circle_2():
    r = Circle(radius=100)
    assert isinstance(r, Circle)
    assert r.area() == 31415.93
    assert r.dimensions() == {"radius": 100}
