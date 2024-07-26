import pytest
from lab_3 import count_vowels
from lab_3 import check_palindrome
from lab_3 import email_id_filter


@pytest.mark.parametrize(
    "x, result",
    [
        ("jP2L9qXhRv3sG5mK6nT8wE0yU4iB7oJ1aF4cD2zS6xN9", 5),
        (
            "The mysterious old book contained ancient secrets and whispered tales of forgotten civilizations buried "
            "beneath the sands of time.",
            44,
        ),
        ("", 0),
        (
            "Underneath the starry night, a gentle breeze rustled the leaves, creating a soothing melody in the quiet "
            "forest",
            35,
        ),
        (
            "In the heart of the bustling city, surrounded by towering skyscrapers and the hum of urban life, "
            "lies a hidden oasis of tranquility. This quaint park, nestled between the concrete giants, "
            "offers a respite from the daily hustle and bustle. Lush greenery, vibrant flowers, and the soothing "
            "melody of chirping birds create a peaceful ambiance that seems almost surreal in this urban jungle. As "
            "people stroll along the winding paths, the stress of the day gradually melts away. Benches strategically "
            "placed beneath ancient trees invite visitors to pause and reflect. The park becomes a canvas for diverse "
            "stories—a meeting place for friends, a sanctuary for solitary readers, a playground for children's "
            "laughter. Each season adds a new layer of beauty, from the vibrant blooms of spring to the rich hues of "
            "autumn leaves. The rhythmic flow of a small stream provides a gentle soundtrack to this haven, "
            "enhancing the sense of serenity. It's a microcosm where time seems to slow down, allowing for moments of "
            "introspection and connection with nature. This urban oasis serves as a reminder that amidst the "
            "fast-paced urban lifestyle, there exist pockets of peace and natural beauty waiting to be discovered by "
            "those willing to wander off the beaten path.",
            375,
        ),
    ],
)
@pytest.mark.timeout(0.3)
def test_count_vowels(x, result):
    assert count_vowels(x) == result


@pytest.mark.parametrize(
    "x, result",
    [
        ("aba", True),
        ("bb", True),
        ("acda", False),
        (
            "vickayakradarstatsmadamnoonreviverreferdeedracecartenetlevelkayakcivicPanamaacanalaplanaman..namanalpalanacaamanaPcivickayakleveltenetracecardeedreferrevivernoonmadamstatsradarkayakciv",
            True,
        ),
        (
            "AmanaplanacanalPanamaradarcivickayakleveltenetracecardeedreferrevivernoonmadamstatsradarkayakciviccivickayakranoonreviverreferdeedracecartenetlevelkayakcivicPanamaacanalaplanaman",
            False,
        ),
    ],
)
@pytest.mark.timeout(0.3)
def test_check_palindrome(x, result):
    assert check_palindrome(x) == result


@pytest.mark.parametrize(
    "x, result",
    [
        (
            [
                "xyz@usc.edu",
                "qwerty@yahoo.com",
                "example@isi.edu",
                "test@gmail.com",
                "dsci510@usc.edu",
            ],
            (3, 2),
        ),
        (
            [],
            (0, 0),
        ),
        (
            [
                "xyz@usc.com",
                "qwerty@yahoo.com",
                "example@isi.com",
                "test@gmail.com",
                "dsci510@usc.edu",
            ],
            (1, 4),
        ),
        (
            [
                "dfgh@usc.com",
            ],
            (0, 1),
        ),
        (
            [
                "iaeuk@yahoo.com",
                "siyqz@usc.edu",
                "cywym@yahoo.com",
                "vmlop@usc.edu",
                "zgfqz@isi.edu",
                "fdznp@gmail.com",
                "jkcfx@gmail.com",
                "taqau@isi.edu",
                "skxbh@yahoo.com",
                "afidp@yahoo.com",
                "plggq@usc.edu",
                "auypy@yahoo.com",
                "evyvo@yahoo.com",
                "jbnzo@yahoo.com",
                "tcfbn@gmail.com",
                "lavhi@usc.edu",
                "otjwp@usc.edu",
                "xesml@usc.edu",
                "ngpep@gmail.com",
                "halmd@gmail.com",
                "wkprr@isi.edu",
                "ejjdh@usc.edu",
                "bhqgx@gmail.com",
                "chpik@yahoo.com",
                "rfgok@gmail.com",
                "pqnti@gmail.com",
                "ruqpf@isi.edu",
                "ncdim@yahoo.com",
                "kljuu@gmail.com",
                "wazrx@usc.edu",
                "vsjtm@yahoo.com",
                "mykrw@yahoo.com",
                "xtgzq@gmail.com",
                "udsoz@usc.edu",
                "fvwup@yahoo.com",
                "cwmgu@gmail.com",
                "nhkis@isi.edu",
                "jzrbj@usc.edu",
                "pixlf@isi.edu",
                "fiyxp@isi.edu",
                "lmjjp@isi.edu",
                "tqncr@gmail.com",
                "vyyea@gmail.com",
                "rfpos@gmail.com",
                "exftm@isi.edu",
                "oxacv@yahoo.com",
                "bnrum@gmail.com",
                "fwjmz@gmail.com",
                "mmwll@gmail.com",
                "agzfa@usc.edu",
                "cutwv@isi.edu",
                "xtrqm@gmail.com",
                "vmrkc@yahoo.com",
                "rnhzf@usc.edu",
                "flsww@yahoo.com",
                "unqmp@usc.edu",
                "xferu@isi.edu",
                "ondvi@yahoo.com",
                "ysdwe@isi.edu",
                "otnec@yahoo.com",
                "wtcdb@yahoo.com",
                "djdmf@yahoo.com",
                "oyfuy@usc.edu",
                "bdlqf@yahoo.com",
                "fgmfz@yahoo.com",
                "ainfy@usc.edu",
                "bmruq@yahoo.com",
                "kyydw@usc.edu",
                "lphvm@gmail.com",
                "rorxn@gmail.com",
                "iqjjm@usc.edu",
                "qvovg@usc.edu",
                "gecic@usc.edu",
                "ebstw@yahoo.com",
                "gtqle@gmail.com",
                "ozvkn@gmail.com",
                "odebw@yahoo.com",
                "iamjx@isi.edu",
                "tijiv@gmail.com",
                "auiam@yahoo.com",
                "revsb@isi.edu",
                "anijn@isi.edu",
                "zrziq@gmail.com",
                "sxwsw@isi.edu",
                "bbgks@yahoo.com",
                "cqset@isi.edu",
                "kxuag@usc.edu",
                "xoajr@gmail.com",
                "kutyx@yahoo.com",
                "gtrlz@usc.edu",
                "fmtzp@yahoo.com",
                "kegpp@usc.edu",
                "fowas@gmail.com",
                "pkauv@yahoo.com",
                "qlqza@isi.edu",
                "ftxer@yahoo.com",
                "fxocy@usc.edu",
                "kcoax@isi.edu",
                "taogo@gmail.com",
                "nrfmt@isi.edu",
            ],
            (43, 57),
        ),
    ],
)
@pytest.mark.timeout(0.3)
def test_email_id_filter(x, result):
    assert email_id_filter(x) == result
