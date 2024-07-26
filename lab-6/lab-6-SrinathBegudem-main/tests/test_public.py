import random
import pytest

from lab_6 import Vehicle
from lab_6 import LibraryMember
from lab_6 import Product


@pytest.mark.timeout(0.3)
def test_vehicle_1():
    car = Vehicle("VIN123", "Toyota", "Camry", 2020)
    assert car.vehicle_id == "VIN123"
    assert car.make == "Toyota"
    assert car.model == "Camry"
    assert car.year == 2020
    assert (
        car.__str__()
        == "Vehicle(vehicle_id='VIN123', make='Toyota', model='Camry', year=2020)"
    )
    assert (
        car.__repr__()
        == "Vehicle(vehicle_id='VIN123', make='Toyota', model='Camry', year=2020)"
    )


@pytest.mark.timeout(0.3)
def test_vehicle_2():
    car = Vehicle("VIN123", "Toyota", "Camry", 2020)
    assert car.vehicle_id == "VIN123"
    assert car.make == "Toyota"
    assert car.model == "Camry"
    assert car.year == 2020
    assert (
        car.__str__()
        == "Vehicle(vehicle_id='VIN123', make='Toyota', model='Camry', year=2020)"
    )
    assert (
        car.__repr__()
        == "Vehicle(vehicle_id='VIN123', make='Toyota', model='Camry', year=2020)"
    )


@pytest.mark.timeout(0.3)
def test_vehicle_3():
    car = Vehicle("VIN234", "Ford", "Mustang", 2021)
    assert car.vehicle_id == "VIN234"
    assert car.make == "Ford"
    assert car.model == "Mustang"
    assert car.year == 2021
    assert (
        car.__str__()
        == "Vehicle(vehicle_id='VIN234', make='Ford', model='Mustang', year=2021)"
    )
    assert (
        car.__repr__()
        == "Vehicle(vehicle_id='VIN234', make='Ford', model='Mustang', year=2021)"
    )


@pytest.mark.timeout(0.3)
def test_vehicle_4():
    car = Vehicle("VIN345", "Ford", "F-150", 2022)
    assert car.vehicle_id == "VIN345"
    assert car.make == "Ford"
    assert car.model == "F-150"
    assert car.year == 2022
    assert (
        car.__str__()
        == "Vehicle(vehicle_id='VIN345', make='Ford', model='F-150', year=2022)"
    )
    assert (
        car.__repr__()
        == "Vehicle(vehicle_id='VIN345', make='Ford', model='F-150', year=2022)"
    )


@pytest.mark.timeout(0.3)
def test_vehicle_5():
    car = Vehicle("VIN456", "Tesla", "Model S", 2023)
    assert car.vehicle_id == "VIN456"
    assert car.make == "Tesla"
    assert car.model == "Model S"
    assert car.year == 2023
    assert (
        car.__str__()
        == "Vehicle(vehicle_id='VIN456', make='Tesla', model='Model S', year=2023)"
    )
    assert (
        car.__repr__()
        == "Vehicle(vehicle_id='VIN456', make='Tesla', model='Model S', year=2023)"
    )


@pytest.mark.timeout(0.3)
def test_library_member_1():
    lm = LibraryMember("001", "Alice")
    assert lm.borrowed_books == []
    assert str(lm) == "LibraryMember(member_id='001', name='Alice', total_borrowed=0)"

    lm.add_book("book1")
    lm.add_book("book2")
    lm.add_book("book3")
    assert lm.count_books() == 3

    lm.remove_book("book1")
    assert lm.count_books() == 2

    assert lm.borrowed_books == ["book2", "book3"]


@pytest.mark.timeout(0.3)
def test_library_member_2():
    lm = LibraryMember("002", "Bob")
    assert lm.borrowed_books == []
    assert str(lm) == "LibraryMember(member_id='002', name='Bob', total_borrowed=0)"

    lm.add_book("book1")
    lm.add_book("book2")
    assert lm.count_books() == 2

    assert lm.borrowed_books == ["book1", "book2"]


@pytest.mark.timeout(0.3)
def test_library_member_3():
    lm = LibraryMember("003", "Charlie")
    assert lm.borrowed_books == []
    assert str(lm) == "LibraryMember(member_id='003', name='Charlie', total_borrowed=0)"

    lm.add_book("book1")
    lm.add_book("book2")
    lm.add_book("book3")
    lm.add_book("book4")
    lm.add_book("book5")
    lm.add_book("book6")
    lm.add_book("book7")
    lm.add_book("book8")
    lm.add_book("book9")
    assert lm.count_books() == 9

    lm.remove_book("book4")
    lm.remove_book("book1")
    lm.remove_book("book8")
    assert lm.count_books() == 6

    assert lm.borrowed_books == ["book2", "book3", "book5", "book6", "book7", "book9"]


@pytest.mark.timeout(0.3)
def test_library_member_4():
    lm = LibraryMember("004", "David")
    assert lm.borrowed_books == []
    assert str(lm) == "LibraryMember(member_id='004', name='David', total_borrowed=0)"

    total = 100
    for i in range(100):
        lm.add_book(f"book{i}")
    assert lm.count_books() == total

    unique_books = {random.randint(10, 89) for _ in range(32)}
    result = total - len(unique_books)
    for i in unique_books:
        lm.remove_book(f"book{i}")
    assert lm.count_books() == result


@pytest.mark.timeout(0.3)
def test_library_member_5():
    # Test for removing a book not borrowed
    lm = LibraryMember("005", "Emma")
    assert lm.borrowed_books == []
    assert str(lm) == "LibraryMember(member_id='005', name='Emma', total_borrowed=0)"

    total = 10000
    for i in range(total):
        lm.add_book(f"book{i}")
    assert lm.count_books() == total

    unique_books = {random.randint(10, 8889) for _ in range(32)}
    result = total - len(unique_books)
    for i in unique_books:
        lm.remove_book(f"book{i}")
    assert lm.count_books() == result


@pytest.mark.timeout(0.3)
def test_product_1():
    prd = Product("12345", "Coffee Mug", 12.99, 100)
    assert str(prd) == (
        "Product(product_code='12345', name='Coffee Mug', price=12.99, "
        "quantity_available=100)"
    )

    prd.update_price(13.00)
    assert prd.price == 13.00

    prd.sell_product(2)
    prd.add_stock(10)
    prd.sell_product(13)
    prd.add_stock(20)
    assert prd.quantity_available == 115


@pytest.mark.timeout(0.3)
def test_product_1():
    prd = Product("12345", "Coffee Mug", 12.99, 100)
    assert (
        str(prd)
        == "Product(product_code='12345', name='Coffee Mug', price=12.99, quantity_available=100)"
    )

    prd.update_price(13.00)
    assert prd.price == 13.00

    prd.sell_product(2)
    prd.add_stock(10)
    prd.sell_product(13)
    prd.add_stock(20)
    assert prd.quantity_available == 115


@pytest.mark.timeout(0.3)
def test_product_2():
    prd = Product("23456", "Notebook", 2.50, 30)
    assert (
        str(prd)
        == "Product(product_code='23456', name='Notebook', price=2.5, quantity_available=30)"
    )

    prd.update_price(4.99)
    assert prd.price == 4.99

    prd.sell_product(100)
    prd.add_stock(150)
    prd.sell_product(2)
    prd.add_stock(12)
    assert prd.quantity_available == 190


@pytest.mark.timeout(0.3)
def test_product_3():
    prd = Product("34567", "Ball", 5.00, 15)
    assert (
        str(prd)
        == "Product(product_code='34567', name='Ball', price=5.0, quantity_available=15)"
    )

    prd.update_price(99.00)
    assert prd.price == 99.00

    prd.sell_product(15)
    assert prd.quantity_available == 0


@pytest.mark.timeout(0.3)
def test_product_4():
    prd = Product("45678", "Pencil", 0.99, 100)
    assert (
        str(prd)
        == "Product(product_code='45678', name='Pencil', price=0.99, quantity_available=100)"
    )

    prd.update_price(99.00)
    assert prd.price == 99.00

    prd.sell_product(87)
    prd.sell_product(1)
    prd.sell_product(33)
    prd.add_stock(34)
    prd.sell_product(33)
    assert prd.quantity_available == 13


@pytest.mark.timeout(0.3)
def test_product_5():
    prd = Product("ABCDE", "T-shirt", 15.00, 20)
    assert (
        str(prd)
        == "Product(product_code='ABCDE', name='T-shirt', price=15.0, quantity_available=20)"
    )

    prd.update_price(4.87)
    assert prd.price == 4.87

    for i in range(20):
        prd.sell_product(1)

    for i in range(90):
        prd.add_stock(i + 1)

    assert prd.quantity_available == 4095
