import os

import pandas as pd
import pytest
from lab_12 import MusicFestival
from lab_12 import Titanic

TEST_DB_NAME = "music_festival.db"


@pytest.mark.timeout(0.5)
def test_music_1():
    if os.path.exists(TEST_DB_NAME):
        os.remove(TEST_DB_NAME)

    obj = MusicFestival()
    obj.create_tables()
    obj.insert_data()

    res = obj.query_1_get_artists_with_rock_genre()
    assert res == ["The Cosmic Keys"]


@pytest.mark.timeout(0.5)
def test_music_2():
    if os.path.exists(TEST_DB_NAME):
        os.remove(TEST_DB_NAME)

    obj = MusicFestival()
    obj.create_tables()
    obj.insert_data()

    res = obj.query_2_total_revenue_from_sales()
    assert res == 739.9


@pytest.mark.timeout(0.5)
def test_music_3():
    if os.path.exists(TEST_DB_NAME):
        os.remove(TEST_DB_NAME)

    obj = MusicFestival()
    obj.create_tables()
    obj.insert_data()

    res = obj.query_3_number_performances()
    assert res == [
        ("Main Stage", 1),
        ("Jazz Corner", 1),
        ("Electronic Dome", 1),
        ("Folk Forest", 1),
        ("Classical Hall", 1),
        ("Blues Bar", 1),
        ("Pop Platform", 1),
        ("Metal Mountain", 1),
        ("Country Corner", 1),
        ("Reggae Room", 1),
    ]


@pytest.mark.timeout(0.5)
def test_music_4():
    if os.path.exists(TEST_DB_NAME):
        os.remove(TEST_DB_NAME)

    obj = MusicFestival()
    obj.create_tables()
    obj.insert_data()

    res = obj.query_4_performances_on_specific_date()
    assert res == [
        ("The Cosmic Keys", "Main Stage", "2023-07-04 12:00"),
        ("Jazz Jaguars", "Jazz Corner", "2023-07-04 12:30"),
        ("Electro Ensemble", "Electronic Dome", "2023-07-04 15:00"),
        ("Folklore Friends", "Folk Forest", "2023-07-04 15:30"),
        ("Reggae Revolution", "Reggae Room", "2023-07-04 16:00"),
        ("Classical Quintet", "Classical Hall", "2023-07-04 18:00"),
        ("Blues Brothers", "Blues Bar", "2023-07-04 18:30"),
        ("Country Cousins", "Country Corner", "2023-07-04 19:00"),
        ("Pop Parade", "Pop Platform", "2023-07-04 21:00"),
        ("Metal Mavericks", "Metal Mountain", "2023-07-04 21:30"),
    ]


@pytest.mark.timeout(0.5)
def test_music_5():
    if os.path.exists(TEST_DB_NAME):
        os.remove(TEST_DB_NAME)

    obj = MusicFestival()
    obj.create_tables()
    obj.insert_data()

    res = obj.query_5_longer_performances()
    assert res == [
        "The Cosmic Keys",
        "Electro Ensemble",
        "Reggae Revolution",
        "Classical Quintet",
        "Pop Parade",
        "Country Cousins",
    ]


@pytest.mark.timeout(0.5)
def test_titanic_1():
    obj = Titanic()

    res = obj.preprocess_data(filename="data/titanic_data.csv")
    assert isinstance(res, pd.DataFrame)
    assert res["Age"].value_counts()[24] == 207


@pytest.mark.timeout(0.5)
def test_titanic_21():
    obj = Titanic()

    data = obj.preprocess_data(filename="data/titanic_data.csv")
    assert obj.get_survived_count(data) == 342


@pytest.mark.timeout(0.5)
def test_titanic_22():
    obj = Titanic()

    data = obj.preprocess_data(filename="data/titanic_data.csv")
    assert 28.32 < obj.get_average_fare(data) < 28.34


@pytest.mark.timeout(0.5)
def test_titanic_23():
    obj = Titanic()

    data = obj.preprocess_data(filename="data/titanic_data.csv")
    assert obj.get_max_age(data) == 80


@pytest.mark.timeout(0.5)
def test_titanic_24():
    obj = Titanic()

    data = obj.preprocess_data(filename="data/titanic_data.csv")
    assert obj.get_min_age(data) == 0.42


@pytest.mark.timeout(0.5)
def test_titanic_25():
    obj = Titanic()

    data = obj.preprocess_data(filename="data/titanic_data.csv")
    assert obj.get_male_count(data) == 577


@pytest.mark.timeout(0.5)
def test_titanic_31():
    obj = Titanic()

    data = obj.preprocess_data(filename="data/titanic_data.csv")
    assert obj.get_died_under_30_count(data) == 353


@pytest.mark.timeout(0.5)
def test_titanic_32():
    obj = Titanic()

    data = obj.preprocess_data(filename="data/titanic_data.csv")
    assert obj.get_passenger_ids(data) == [
        8,
        12,
        17,
        21,
        25,
        31,
        42,
        49,
        54,
        59,
        64,
        65,
        79,
        94,
        99,
        100,
        110,
        118,
        129,
        134,
        137,
        149,
        166,
        168,
        169,
        172,
        177,
        178,
        180,
        185,
        188,
        194,
        195,
        212,
        218,
        230,
        237,
        238,
        250,
        253,
        255,
        260,
        264,
        272,
        274,
        278,
        279,
        280,
        285,
        296,
        302,
        303,
        309,
        313,
        315,
        317,
        324,
        329,
        331,
        332,
        341,
        361,
        362,
        375,
        398,
        406,
        410,
        414,
        420,
        425,
        427,
        428,
        431,
        433,
        441,
        448,
        451,
        453,
        457,
        461,
        467,
        468,
        473,
        477,
        482,
        486,
        488,
        507,
        508,
        509,
        513,
        518,
        519,
        531,
        534,
        536,
        537,
        544,
        546,
        547,
        549,
        552,
        556,
        566,
        568,
        573,
        583,
        595,
        596,
        598,
        601,
        605,
        634,
        635,
        638,
        643,
        652,
        663,
        675,
        695,
        702,
        706,
        708,
        712,
        727,
        729,
        733,
        747,
        751,
        769,
        775,
        784,
        788,
        789,
        792,
        797,
        800,
        802,
        807,
        812,
        816,
        820,
        823,
        840,
        855,
        858,
        863,
        875,
        881,
        886,
        889,
    ]


@pytest.mark.timeout(0.5)
def test_titanic_33():
    obj = Titanic()

    data = obj.preprocess_data(filename="data/titanic_data.csv")
    assert obj.get_survivors_classwise(data) == {1: 136, 2: 87, 3: 119}


@pytest.mark.timeout(0.5)
def test_titanic_34():
    obj = Titanic()

    data = obj.preprocess_data(filename="data/titanic_data.csv")
    assert set(obj.get_passenger_names(data)) == {
        'Angle, Mrs. William A (Florence "Mary" Agnes Hughes)',
        "Ball, Mrs. (Ada E Hall)",
        "Brown, Mrs. Thomas William Solomon (Elizabeth Catherine Ford)",
        "Buss, Miss. Kate",
        "Bystrom, Mrs. (Karolina)",
        "Cameron, Miss. Clear Annie",
        "Carter, Mrs. Ernest Courtenay (Lilian Hughes)",
        "Collyer, Mrs. Harvey (Charlotte Annie Tate)",
        "Doling, Mrs. John T (Ada Julia Bone)",
        "Drew, Mrs. James Vivian (Lulu Thorne Christian)",
        "Funk, Miss. Annie Clemmer",
        "Garside, Miss. Ethel",
        "Hart, Mrs. Benjamin (Esther Ada Bloomfield)",
        "Herman, Mrs. Samuel (Jane Laver)",
        "Hewlett, Mrs. (Mary D Kingcome) ",
        "Hocking, Mrs. Elizabeth (Eliza Needs)",
        'Kelly, Mrs. Florence "Fannie"',
        "Lemore, Mrs. (Amelia Milley)",
        "Louch, Mrs. Charles Alexander (Alice Adelaide Slow)",
        "Mack, Mrs. (Mary)",
        "Mellinger, Mrs. (Elizabeth Anne Maidment)",
        "Parrish, Mrs. (Lutie Davis)",
        "Pinsky, Mrs. (Rosa)",
        "Quick, Mrs. Frederick Charles (Jane Richards)",
        "Ridsdale, Miss. Lucy",
        "Smith, Miss. Marion Elsie",
        "Toomey, Miss. Ellen",
        'Watt, Mrs. James (Elizabeth "Bessie" Inglis Milne)',
        "Webber, Miss. Susan",
        "West, Mrs. Edwy Arthur (Ada Mary Worth)",
    }


@pytest.mark.timeout(0.5)
def test_titanic_35():
    obj = Titanic()

    data = obj.preprocess_data(filename="data/titanic_data.csv")
    assert (
        obj.get_oldest_survived_passenger(data)
        == "Barkworth, Mr. Algernon Henry Wilson"
    )
