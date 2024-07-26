# Test cases
import pytest
import unittest
import os
import json
import xmltodict

from lab_9 import sky_scraper
from lab_9 import land_scraper


@pytest.mark.timeout(10)
class TestSkyScraper(unittest.TestCase):
    def setUp(self):
        self.url = "https://en.wikipedia.org/wiki/List_of_spaceflight_launches_in_January%E2%80%93June_2022"
        self.json_file = None

    def test_sky_scraper(self):
        self.json_file = sky_scraper(self.url)

        self.assertTrue(os.path.exists(self.json_file))

        with open(self.json_file, "r") as f:
            data = json.load(f)

        self.assertIsInstance(data, list)

        expected_keys = [
            "datetime",
            "country",
            "rocket",
            "flight_number",
            "launch_site",
            "lsp",
            "payload",
        ]

        expected_payload_keys = [
            "satellite",
            "country",
            "operator",
            "orbit",
            "function",
            "decay",
            "outcome",
        ]

        for launch in data:
            for key in expected_keys:
                self.assertIn(key, launch)

            payload = launch["payload"]
            self.assertIn(len(payload), [32, 1, 2, 3, 4, 6, 7, 10, 46, 16, 18])

            for pld in payload:
                for key in expected_payload_keys:
                    self.assertIn(key, pld)

    def tearDown(self):
        if self.json_file:
            os.remove(self.json_file)


@pytest.mark.timeout(10)
def test_land_scraper_1():
    xml_file = land_scraper("data/cities_1.txt")
    data_dict = xmltodict.parse(open(xml_file).read())

    assert data_dict == {
        "cities": {
            "city": [
                {
                    "name": "Los Angeles",
                    "latitude": "34.0536909",
                    "longitude": "-118.242766",
                },
                {
                    "name": "San Francisco",
                    "latitude": "37.7792588",
                    "longitude": "-122.4193286",
                },
                {
                    "name": "Phoenix",
                    "latitude": "33.4484367",
                    "longitude": "-112.074141",
                },
                {
                    "name": "New York",
                    "latitude": "40.7127281",
                    "longitude": "-74.0060152",
                },
                {"name": "Boston", "latitude": "42.3554334", "longitude": "-71.060511"},
                {
                    "name": "Seattle",
                    "latitude": "47.6038321",
                    "longitude": "-122.330062",
                },
                {"name": "Miami", "latitude": "25.7741728", "longitude": "-80.19362"},
            ]
        }
    }

    if xml_file:
        os.remove(xml_file)


@pytest.mark.timeout(10)
def test_land_scraper_2():
    xml_file = land_scraper("data/cities_2.txt")
    data_dict = xmltodict.parse(open(xml_file).read())

    assert data_dict == {
        "cities": {
            "city": [
                {
                    "name": "San Diego",
                    "latitude": "32.7174202",
                    "longitude": "-117.162772",
                },
                {
                    "name": "Las Vegas",
                    "latitude": "36.1672559",
                    "longitude": "-115.148516",
                },
                {
                    "name": "Chicago",
                    "latitude": "41.8755616",
                    "longitude": "-87.6244212",
                },
                {
                    "name": "Denver",
                    "latitude": "39.7392364",
                    "longitude": "-104.984862",
                },
                {
                    "name": "Atlanta",
                    "latitude": "33.7489924",
                    "longitude": "-84.3902644",
                },
            ]
        }
    }
    if xml_file:
        os.remove(xml_file)


@pytest.mark.timeout(20)
def test_land_scraper_3():
    xml_file = land_scraper("data/cities_3.txt")
    data_dict = xmltodict.parse(open(xml_file).read())

    assert data_dict == {
        "cities": {
            "city": [
                {
                    "name": "Vancouver",
                    "latitude": "49.2608724",
                    "longitude": "-123.113952",
                },
                {
                    "name": "Dayton",
                    "latitude": "39.7589478",
                    "longitude": "-84.1916069",
                },
                {
                    "name": "Chula Vista",
                    "latitude": "32.6400541",
                    "longitude": "-117.084195",
                },
                {
                    "name": "Killeen",
                    "latitude": "31.1171441",
                    "longitude": "-97.727796",
                },
                {
                    "name": "Rockford",
                    "latitude": "42.2713945",
                    "longitude": "-89.093966",
                },
                {
                    "name": "Amarillo",
                    "latitude": "35.2072185",
                    "longitude": "-101.833824",
                },
                {
                    "name": "McKinney",
                    "latitude": "33.1976496",
                    "longitude": "-96.6154471",
                },
                {
                    "name": "New Haven",
                    "latitude": "41.3082138",
                    "longitude": "-72.9250518",
                },
                {
                    "name": "Bridgeport",
                    "latitude": "41.1792695",
                    "longitude": "-73.1887863",
                },
                {
                    "name": "Paterson",
                    "latitude": "40.9167654",
                    "longitude": "-74.171811",
                },
                {
                    "name": "Billings",
                    "latitude": "45.7874957",
                    "longitude": "-108.49607",
                },
                {
                    "name": "Manchester",
                    "latitude": "53.4794892",
                    "longitude": "-2.2451148",
                },
                {"name": "Fargo", "latitude": "46.877229", "longitude": "-96.789821"},
                {
                    "name": "Sioux Falls",
                    "latitude": "43.5476008",
                    "longitude": "-96.7293629",
                },
                {
                    "name": "Cape Coral",
                    "latitude": "26.5625742",
                    "longitude": "-81.9438802",
                },
                {
                    "name": "Waterbury",
                    "latitude": "41.5538091",
                    "longitude": "-73.0438362",
                },
                {
                    "name": "Montgomery",
                    "latitude": "32.3669656",
                    "longitude": "-86.3006485",
                },
                {
                    "name": "Cedar Rapids",
                    "latitude": "41.9758872",
                    "longitude": "-91.6704053",
                },
                {
                    "name": "Sterling Heights",
                    "latitude": "42.5803122",
                    "longitude": "-83.0302033",
                },
            ]
        }
    }
    if xml_file:
        os.remove(xml_file)
