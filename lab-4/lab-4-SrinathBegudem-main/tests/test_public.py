import random

import pytest
import os
from lab_4 import analyze_climate_data
from lab_4 import rainfall_prediction
from lab_4 import export_weather_predictions


@pytest.mark.parametrize(
    "x, result",
    [
        ("data/weather_1.csv", (15, 15, -2.6, 47.4, 63.2, 8.54)),
        ("data/weather_2.csv", (2999, 1006, -3.0, 45.8, 74.7, 2.0)),
        ("data/weather_3.csv", (2000, 652, -2.8, 44.8, 74.62, 1.99)),
        ("data/weather_4.csv", (215, 214, -2.9, 48.7, 62.9, 7.78)),
        ("data/weather_5.csv", (20000, 19927, -3.0, 49.0, 63.52, 7.8)),
    ],
)
@pytest.mark.timeout(0.3)
def test_analyze_climate_data(x, result):
    assert analyze_climate_data(x) == result


@pytest.mark.parametrize(
    "x, result",
    [
        ("data/weather_1.csv", (12, 12)),
        ("data/weather_2.csv", (1936, 929)),
        ("data/weather_3.csv", (1239, 613)),
        ("data/weather_4.csv", (150, 149)),
        ("data/weather_5.csv", (13999, 13966)),
    ],
)
@pytest.mark.timeout(0.3)
def test_rainfall_prediction(x, result):
    assert rainfall_prediction(x) == result


@pytest.mark.parametrize(
    "x, y",
    [
        ("data/weather_1.csv", "data/weather_1_pred.csv"),
        ("data/weather_2.csv", "data/weather_2_pred.csv"),
        ("data/weather_3.csv", "data/weather_3_pred.csv"),
        ("data/weather_4.csv", "data/weather_4_pred.csv"),
        ("data/weather_5.csv", "data/weather_5_pred.csv"),
    ],
)
@pytest.mark.timeout(0.3)
def test_export_weather_predictions(x, y):
    assert export_weather_predictions(x, y) is None
    assert os.path.exists(y) is True
    data_x = open(x).readlines()
    data_y = open(y).readlines()
    assert len(data_x) == len(data_y)
    assert len(data_y[random.randint(0, len(data_x))].split(",")) == 5
