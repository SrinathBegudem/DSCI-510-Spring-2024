# Test cases
import pytest

from lab_8 import count_unique_words
from lab_8 import get_books_data


@pytest.mark.timeout(5)
def test_count_unique_words_1():
    url = "https://data.pr4e.org/clown.txt"
    assert count_unique_words(url) == 11


@pytest.mark.timeout(5)
def test_count_unique_words_2():
    assert count_unique_words("https://data.pr4e.org/romeo.txt") == 26


@pytest.mark.timeout(5)
def test_count_unique_words_3():
    assert count_unique_words("https://data.pr4e.org/romeo-full.txt") == 543


@pytest.mark.timeout(5)
def test_count_unique_words_4():
    assert count_unique_words("https://data.pr4e.org/intro.txt") == 1030


@pytest.mark.timeout(5)
def test_count_unique_words_5():
    assert count_unique_words("https://data.pr4e.org/mbox.txt") == 27645


@pytest.mark.timeout(5)
def test_count_unique_words_5():
    assert count_unique_words("https://data.pr4e.org/romeo-full.txt") == 543


@pytest.mark.timeout(5)
def test_get_books_data_1():
    assert get_books_data("http://books.toscrape.com") == [
        {"price": 51.77, "title": "A Light in the Attic"},
        {"price": 53.74, "title": "Tipping the Velvet"},
        {"price": 50.1, "title": "Soumission"},
        {"price": 47.82, "title": "Sharp Objects"},
        {"price": 54.23, "title": "Sapiens: A Brief History of Humankind"},
        {"price": 22.65, "title": "The Requiem Red"},
        {"price": 33.34, "title": "The Dirty Little Secrets of Getting Your Dream Job"},
        {
            "price": 17.93,
            "title": "The Coming Woman: A Novel Based on the Life of the Infamous "
            "Feminist, Victoria Woodhull",
        },
        {
            "price": 22.6,
            "title": "The Boys in the Boat: Nine Americans and Their Epic Quest for Gold "
            "at the 1936 Berlin Olympics",
        },
        {"price": 52.15, "title": "The Black Maria"},
        {"price": 13.99, "title": "Starving Hearts (Triangular Trade Trilogy, #1)"},
        {"price": 20.66, "title": "Shakespeare's Sonnets"},
        {"price": 17.46, "title": "Set Me Free"},
        {
            "price": 52.29,
            "title": "Scott Pilgrim's Precious Little Life (Scott Pilgrim #1)",
        },
        {"price": 35.02, "title": "Rip it Up and Start Again"},
        {
            "price": 57.25,
            "title": "Our Band Could Be Your Life: Scenes from the American Indie "
            "Underground, 1981-1991",
        },
        {"price": 23.88, "title": "Olio"},
        {
            "price": 37.59,
            "title": "Mesaerion: The Best Science Fiction Stories 1800-1849",
        },
        {"price": 51.33, "title": "Libertarianism for Beginners"},
        {"price": 45.17, "title": "It's Only the Himalayas"},
    ]


@pytest.mark.timeout(5)
def test_get_books_data_2():
    assert get_books_data(
        "https://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html"
    ) == [
        {
            "price": 52.29,
            "title": "Scott Pilgrim's Precious Little Life (Scott Pilgrim #1)",
        },
        {
            "price": 16.28,
            "title": "Tsubasa: WoRLD CHRoNiCLE 2 (Tsubasa WoRLD CHRoNiCLE #2)",
        },
        {"price": 19.49, "title": "This One Summer"},
        {"price": 38.16, "title": "The Nameless City (The Nameless City #1)"},
        {"price": 51.04, "title": "Saga, Volume 5 (Saga (Collected Editions) #5)"},
        {
            "price": 50.4,
            "title": "Rat Queens, Vol. 3: Demons (Rat Queens (Collected Editions) "
            "#11-15)",
        },
        {
            "price": 13.61,
            "title": "Princess Jellyfish 2-in-1 Omnibus, Vol. 01 (Princess Jellyfish "
            "2-in-1 Omnibus #1)",
        },
        {"price": 18.97, "title": "Pop Gun War, Volume 1: Gift"},
        {"price": 10.16, "title": "Patience"},
        {
            "price": 15.44,
            "title": "Outcast, Vol. 1: A Darkness Surrounds Him (Outcast #1)",
        },
        {
            "price": 48.41,
            "title": "orange: The Complete Collection 1 (orange: The Complete Collection "
            "#1)",
        },
        {
            "price": 46.91,
            "title": "Lumberjanes, Vol. 2: Friendship to the Max (Lumberjanes #5-8)",
        },
        {
            "price": 45.61,
            "title": "Lumberjanes, Vol. 1: Beware the Kitten Holy (Lumberjanes #1-4)",
        },
        {
            "price": 19.92,
            "title": "Lumberjanes Vol. 3: A Terrible Plan (Lumberjanes #9-12)",
        },
        {
            "price": 29.17,
            "title": "I Hate Fairyland, Vol. 1: Madly Ever After (I Hate Fairyland "
            "(Compilations) #1-5)",
        },
        {"price": 54.63, "title": "I am a Hero Omnibus Volume 1"},
        {"price": 22.11, "title": "Giant Days, Vol. 2 (Giant Days #5-8)"},
        {"price": 51.99, "title": "Danganronpa Volume 1"},
        {
            "price": 36.72,
            "title": "Codename Baboushka, Volume 1: The Conclave of Death",
        },
        {"price": 17.08, "title": "Camp Midnight"},
    ]


@pytest.mark.timeout(5)
def test_get_books_data_3():
    assert get_books_data(
        "https://books.toscrape.com/catalogue/category/books/humor_30/index.html"
    ) == [
        {"price": 44.07, "title": "The Long Haul (Diary of a Wimpy Kid #9)"},
        {"price": 11.83, "title": "Old School (Diary of a Wimpy Kid #10)"},
        {
            "price": 25.98,
            "title": "I Know What I'm Doing -- and Other Lies I Tell Myself: Dispatches "
            "from a Life Under Construction",
        },
        {
            "price": 14.75,
            "title": "Hyperbole and a Half: Unfortunate Situations, Flawed Coping "
            "Mechanisms, Mayhem, and Other Things That Happened",
        },
        {"price": 43.68, "title": "Dress Your Family in Corduroy and Denim"},
        {"price": 25.55, "title": "Toddlers Are A**holes: It's Not Your Fault"},
        {"price": 30.89, "title": "When You Are Engulfed in Flames"},
        {"price": 31.69, "title": "Naked"},
        {
            "price": 55.5,
            "title": "Lamb: The Gospel According to Biff, Christ's Childhood Pal",
        },
        {"price": 51.07, "title": "Holidays on Ice"},
    ]


@pytest.mark.timeout(5)
def test_get_books_data_4():
    assert get_books_data(
        "https://books.toscrape.com/catalogue/category/books/childrens_11/page-2.html"
    ) == [
        {"price": 16.26, "title": "The Cat in the Hat (Beginner Books B-1)"},
        {"price": 28.54, "title": "Red: The True Story of Red Riding Hood"},
        {"price": 37.52, "title": "Horrible Bear!"},
        {"price": 10.79, "title": "Green Eggs and Ham (Beginner Books B-16)"},
        {"price": 10.62, "title": "Counting Thyme"},
        {"price": 10.66, "title": "Are We There Yet?"},
        {
            "price": 52.88,
            "title": "Diary of a Minecraft Zombie Book 1: A Scare of a Dare (An "
            "Unofficial Minecraft Book)",
        },
        {"price": 28.34, "title": "Matilda"},
        {
            "price": 22.85,
            "title": "Charlie and the Chocolate Factory (Charlie Bucket #1)",
        },
    ]


@pytest.mark.timeout(5)
def test_get_books_data_5():
    assert get_books_data(
        "https://books.toscrape.com/catalogue/category/books/spirituality_39/index.html"
    ) == [
        {
            "price": 17.66,
            "title": "The Four Agreements: A Practical Guide to Personal Freedom",
        },
        {
            "price": 32.24,
            "title": "The Activist's Tao Te Ching: Ancient Advice for a Modern "
            "Revolution",
        },
        {"price": 37.8, "title": "Chasing Heaven: What Dying Taught Me About Living"},
        {
            "price": 20.91,
            "title": "If I Gave You God's Phone Number....: Searching for Spirituality "
            "in America",
        },
        {
            "price": 46.33,
            "title": "Unreasonable Hope: Finding Faith in the God Who Brings Purpose to "
            "Your Pain",
        },
        {"price": 55.65, "title": "A New Earth: Awakening to Your Life's Purpose"},
    ]
