import pytest
from lab_2 import education_details
from lab_2 import yearly_allowance
from lab_2 import conversion_to_british_pound
from lab_2 import yearly_profit
from lab_2 import percentage_change


@pytest.mark.parametrize(
    "x, y, result",
    [
        ("Data Science", 2025, "Data Science, 2025"),
        ("Business Analytics", 2023, "Business Analytics, 2023"),
        ("Journalism", 2026, "Journalism, 2026"),
        ("Arts and Science", 2027, "Arts and Science, 2027"),
        ("Architecture", 2028, "Architecture, 2028"),
    ],
)
@pytest.mark.timeout(0.3)
def test_education_details(capsys, x, y, result):
    education_details(x, y)
    assert capsys.readouterr().out.strip() == result


@pytest.mark.parametrize(
    "x, y, z, result",
    [
        (15, 40, 52, 31200),
        (25, 36, 52, 46800),
        (37.5, 22, 52, 42900),
        (31.15, 20, 52, 32396),
        (17, 12, 52, 10608),
    ],
)
@pytest.mark.timeout(0.3)
def test_yearly_allowance(x, y, z, result):
    assert yearly_allowance(x, y, z) == result


@pytest.mark.parametrize(
    "x, result",
    [
        (31200, 24960.0),
        (46800, 37440.0),
        (42900, 34320.0),
        (32396, 25916.8),
        (10608, 8486.4),
    ],
)
@pytest.mark.timeout(0.3)
def test_conversion_to_british_pound(x, result):
    assert conversion_to_british_pound(x) == result


@pytest.mark.parametrize(
    "x, y, result",
    [
        (253, 365, 92345),
        (231, 366, 84546),
        (290, 365, 105850),
        (310, 366, 113460),
        (999, 365, 364635),
    ],
)
@pytest.mark.timeout(0.3)
def test_yearly_profit(x, y, result):
    assert yearly_profit(x, y) == result


@pytest.mark.parametrize(
    "x, y, result",
    [
        (92345, 120000, "23.05% loss"),
        (84546, 150000, "43.64% loss"),
        (105850, 90000, "17.61% profit"),
        (113460, 120000, "5.45% loss"),
        (364635, 150000, "143.09% profit"),
    ],
)
@pytest.mark.timeout(0.3)
def test_percentage_change(x, y, result):
    assert percentage_change(x, y).strip() == result
