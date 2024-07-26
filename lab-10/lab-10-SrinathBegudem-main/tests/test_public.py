import pytest

from lab_10 import redact_phone_numbers
from lab_10 import validate_passwords
from lab_10 import extract_host_from_url


@pytest.mark.timeout(0.3)
def test_redact_phone_numbers_1():
    text = "Call me at 123-456-7890 or 098-765-4321 tomorrow."
    assert redact_phone_numbers(text).count("[REDACTED]") == 2


@pytest.mark.timeout(0.3)
def test_redact_phone_numbers_2():
    text = "No phone numbers in this text."
    assert redact_phone_numbers(text) == text


@pytest.mark.timeout(0.3)
def test_redact_phone_numbers_3():
    text = """In the heart of the bustling city, where the sounds of traffic and people create a constant hum, 
    lies a small café tucked away 123-456-7890 in a quiet corner. The aroma of freshly brewed coffee wafts through the air, 
    mingling with the scent of freshly baked pastries. The café is a sanctuary for those seeking a moment of respite 
    from the chaos of the outside world. 123-456-7843 Patrons sit at small tables, lost in conversation or engrossed in books, 
    their faces illuminated by the warm glow of the overhead lights. Baristas behind the counter expertly craft each 
    cup of coffee with care, their movements fluid and precise. Soft music plays in the background, adding to the 
    ambiance of the space. Outside, the city bustles with life, but 123-765-7890 within the walls of the café, time seems to slow 
    down. It's a place where friendships are forged over shared cups of coffee and where strangers find solace in the 
    simple act of sitting together in silence. As the day turns to night, the café 213-980-7890 takes on a different energy, 
    with dim lighting casting 112-421-2828 shadows on the walls and candles flickering on the tables. It becomes a haven for those 
    seeking refuge from the darkness outside, a beacon of warmth and light in a 213-213-7890 world that can sometimes feel cold 
    and harsh."""
    assert redact_phone_numbers(text).count("[REDACTED]") == 6


@pytest.mark.timeout(0.3)
def test_redact_phone_numbers_4():
    text = """In the heart of the bustling city, where the sounds of traffic and people create a constant hum, 
    lies a small café tucked away 123-456-7890 in a quiet corner. The aroma of freshly brewed coffee wafts through the air, 
    mingling with the scent of freshly baked pastries. The café is a sanctuary for those seeking a moment of respite 
    from the chaos of the outside world. 123-456-7843 Patrons 777-888-9999 sit at small tables, lost in conversation or engrossed in books, 
    their faces illuminated by the warm glow of the overhead lights. Baristas 555-123-4567 behind the counter expertly craft each 
    cup of coffee with care, their movements fluid and precise. Soft music plays in the background, adding to the 
    ambiance of the space. Outside, the city bustles with life, but 123-765-7890 within the walls of the café, time seems to slow 
    down. It's a place where friendships are forged over shared cups of coffee and where strangers find solace in the 
    simple act of sitting together in silence. As the day turns to night, the café 213-980-7890 takes on a different energy, 
    with dim lighting 098-765-4321 casting 112-421-2828 shadows on the walls and candles flickering on the tables. It becomes a haven for those 
    seeking refuge from the darkness outside, a beacon of warmth and light in a 213-213-7890 world that can sometimes feel cold 
    and harsh.

    Amidst the hustle and bustle of the city streets, the café stands as a quiet oasis, a place where one can escape 
    the demands of daily life and simply be. 321-654-9870 Whether it's sipping a steaming cup of coffee on a rainy afternoon 
    or enjoying a leisurely brunch with friends on a sunny day, the café offers a sense of comfort and familiarity 
    that is hard to find elsewhere. 555-444-3333 The walls are adorned with artwork from local artists, adding to the 
    charm and character of the space. 999-888-7777 The menu features a variety of delicious options, from classic 
    breakfast dishes to inventive sandwiches and salads. 123-123-1234 There's something for everyone to enjoy, whether 
    you're a coffee aficionado or a tea enthusiast. 321-321-4321 And with free Wi-Fi available, it's the perfect spot 
    for catching up on work or studying for exams. 555-888-9999 The café is more than just a place to grab a cup of coffee; 
    it's a community hub where people come together to connect, relax, and recharge. 555-555-5555 It's a place where 
    memories are made and stories are shared, a place that holds a special 213-213-7890 place in the hearts of all who 
    visit."""

    assert redact_phone_numbers(text).count("[REDACTED]") == 17


@pytest.mark.timeout(0.3)
def test_redact_phone_numbers_5():
    text = """In the heart of the bustling city, where the sounds of traffic and people create a constant hum, 
    lies a small café tucked away 123456-7890 in a quiet corner. The aroma of freshly brewed coffee wafts through the air, 
    mingling with the scent of freshly baked pastries. The café is a sanctuary for those seeking a moment of respite 
    from the chaos of the outside world. 123-456-7843 Patrons sit at small tables, lost in conversation or engrossed in books, 
    their faces illuminated by the warm glow of the overhead lights. Baristas behind the counter expertly craft each 
    cup of coffee with care, their movements fluid and precise. Soft music plays in the background, adding to the 
    ambiance of the space. Outside, the city bustles with life, but 123765-7890 within the walls of the café, time seems to slow 
    down. It's a place where friendships are forged over shared cups of coffee and where strangers find solace in the 
    simple act of sitting together in silence. As the day turns to night, the café 213-9807890 takes on a different energy, 
    with dim lighting casting 112-421-2828 shadows on the walls and candles flickering on the tables. It becomes a haven for those 
    seeking refuge from the darkness outside, a beacon of warmth and light in a 213-213-7890 world that can sometimes feel cold 
    and harsh."""
    assert redact_phone_numbers(text).count("[REDACTED]") == 3


@pytest.mark.timeout(0.3)
def test_validate_passwords_1():
    pwd = ["StrongPass1!", "weak", "12345", "AnotherStrongPass2@"]
    res = validate_passwords(pwd)
    assert isinstance(res, list)
    assert res.count(True) == 2
    assert res.count(False) == 2


@pytest.mark.timeout(0.3)
def test_validate_passwords_2():
    pwd = []
    res = validate_passwords(pwd)
    assert isinstance(res, list)
    assert len(res) == 0


@pytest.mark.timeout(0.3)
def test_validate_passwords_3():
    pwd = [
        "O2#PsKQP7Doe",
        "1(g)BI8!7!XI",
        "weak",
        "8RbMAwbhRXOw",
        "7VagPKbluRZN",
        "lz4%@oJWKoMW",
        "12345",
        "StrongPass1!",
        "vzySseUkoR%1",
        "AnotherStrongPass2@",
        "6cfJaXN7hA1@",
        "IfV&4)8QudVU",
        "!*AAjdY(bMsg",
        "abc123",
        "password",
    ]

    res = validate_passwords(pwd)
    assert isinstance(res, list)
    assert res.count(True) == 8
    assert res.count(False) == 7


@pytest.mark.timeout(0.3)
def test_validate_passwords_4():
    pwd = [
        "lQIqX(r4e#Ge",
        "qwerty",
        "(9NsQUgJ@ouI",
        "123abc",
        "9xYa9T1oUZxf",
        "qwerty",
        "StrongPass1!",
        "password",
        "123abc",
        "Ysh2whvO25s3",
        "qwerty",
        "123abc",
        "99A%S$PP%)!e",
        "password",
        "Y@Qk1EX49Qpw",
        "abc123",
        "qwerty",
        "abc123",
        "123abc",
        "VpMp8zGHFzTw",
        "abc123",
        "123abc",
        "IQ&$ICTbT4bE",
        "7AidAs##eUU)",
        "123abc",
        "F3Noh72c^9iH",
        "abc123",
        "L0M2#Jxqyazz",
        "abc123",
        "password",
        "6dzT&kSZv@)L",
        "123abc",
        "qwerty",
        "password",
        "12345",
        "qwerty",
        "0G42xPGyJ9w4",
        "123abc",
        "oM5Hca3@TJge",
        "password",
        "123abc",
        "odFXsI3ez1G@",
        "abc123",
        "3z&i8u*1zF)Q",
        "ru)XNnD5sZy!",
        "password",
        "sSbfUNDsJQ1o",
        "pN^Zh#tzZi^g",
        "password",
        "!$lsZGBvt&m9",
        "3hu3xxdoYgz!",
        "0QLow4!NVZjN",
        "5VZNhDa*Tlx1",
        "h!jwrjc8U!p&",
        "abc123",
        "abc123",
        "weak",
        "abc123",
        "AnotherStrongPass2@",
        "qwerty",
        "uOeZKsuXeCB)",
        "15(ck!7nN2Hp",
        "H3CceKHZfIk3",
        "@eCSR#xdB!d#",
        "oUddJe(E4YwU",
        "$bPSULEuEMza",
        "abc123",
        "cQ*Mr3V8K!$s",
        "qwerty",
        "j35THoiF7Pe)",
        "password",
        "123abc",
        "U8ZYpe7Az5K^",
        "9lCdE*4g#@K6",
        "abc123",
        "password",
        "abc123",
        "q6emM)BoGY!b",
        "4AZ$fCJVkuXK",
        "123abc",
        "VCPfr*vPU9Ax",
        "mcIRNfdeIr4)",
        "qwerty",
        "3q@NdxIgFDhG",
        "iB(*nOQNC9y9",
        "k6sUJO$NSh*u",
        "impwr^jH8Rdd",
        "v@ZH9eAK%zMd",
        "($l2yPzSLAC2",
        "J6J%aI&zbIC7",
        "9GURmM9kNnOU",
        "Suv2aM8o4XiN",
        "abc123",
        "qwerty",
        "123abc",
        "NPzH$vq)dzqU",
        "123abc",
        "z$7A&TGxpM@P",
        "password",
        "L8QVF(k!K)YV",
    ]

    res = validate_passwords(pwd)
    assert isinstance(res, list)
    assert res.count(True) == 39
    assert res.count(False) == 61


@pytest.mark.timeout(0.3)
def test_validate_passwords_5():
    pwd = [
        "xT2aly9YO06H",
        "qwerty",
        "password",
        "Xk4H$7WrUuGq",
        "abc123",
        "qwerty",
        "OjtOTwMMmi*5",
        "GZfjq%t&EP7L",
        "abc123",
        "Fh&GhZQdxQQJ",
        "abc123",
        "123abc",
        "pbpumYz5rA(&",
        "123abc",
        "valA3!l4S1AK",
        "wngsweL!Fu7f",
        "abc123",
        "123abc",
        "Ov$of*!iftCi",
        "0IkD5auMXk&g",
        "123abc",
        "qwerty",
        "nedf42jWnLRd",
        "qwerty",
        "qwerty",
        "*cw!QzW$jpR6",
        "123abc",
        "za^iV9bEjQqm",
        "abc123",
        "1$NBinIQPEhp",
        "wi!RVkV5Tarv",
        "*8MiuSHW2$es",
        "abc123",
        "cThsk0yIlE5c",
        "password",
        "password",
        "qwerty",
        "*L4Muz0ZyDMZ",
        "abc123",
        "qwerty",
        "qwerty",
        "password",
        "abc123",
        "D@zsKnHlZVey",
        "GaHdLrDysocc",
        "password",
        "abc123",
        "password",
        "password",
        "mGZ1ac2Sgr&t",
        "CPxY&KXv(WZn",
        "caryqi)i0x#$",
        "6LcYn9AVi324",
        "123abc",
        "PnJpk$IfH#*z",
        "qwerty",
        "yxAJe*rDvatM",
        "7UgK6oVcEvAS",
        "@yU%5!FfyBrc",
        "1JFigtd(XBeE",
        "VQFt1en^j18x",
        "Y^o)s^76112V",
        "485n6B(3V8v$",
        "3J4tGlsOrNs)",
        "fDr#iEl&XGlw",
        "qwerty",
        "wZO@9zlc5ZVY",
        "abc123",
        "password",
        "qwerty",
        "C3&KXU$kRJc&",
        "rQMk3x4Ehz!*",
        "kebAvGNaopt5",
        "abc123",
        "password",
        "w&gN0NAd1QBE",
        "qwerty",
        "password",
        "AlWKQT49iYqA",
        "abc123",
        "qwerty",
        "yi*!DxJywLCQ",
        "qwerty",
        "(AdQJWmm4oQe",
        "qwerty",
        "qwerty",
        "7BRfH8$GkrdS",
        "password",
        "password",
        "password",
        "123abc",
        "^SpoTOgXnNQl",
        "ssYgoUdIv(TJ",
        "RpEo^yds^ZE@",
        "UQOLvrsD)^1N",
        "UFGh2RsAIUID",
        "abc123",
        "abc123",
        "password",
        "123abc",
        "password",
        "abc123",
        "qwerty",
        "A8sIoegcGzie",
        "^B%nlTzjp&Df",
        "ZJh(XdB8WcuD",
        "qwerty",
        "qwerty",
        "password",
        "7krEFyonunh%",
        "qwerty",
        "abc123",
        "%ggQf$o&3$hv",
        "password",
        "password",
        "l3a#2ULaKr^#",
        "qwerty",
        "0Hb#k%BTE&VN",
        "abc123",
        "gDL^wiYQUyZU",
        "sM1Z5VK7WVk9",
        "f$&3(#KO%IFn",
        "dPA5Xc&v$F9s",
        "abc123",
        "abc123",
        "123abc",
        "3UsGB)7eo4a!",
        "qwerty",
        "abc123",
        "123abc",
        "82UAPahGGz@9",
        "SPqkCi4mXa8%",
        "123abc",
        "abc123",
        "password",
        "WQygu#qAsXC^",
        "123abc",
        "qwerty",
        "3yzHHJtZ%ykt",
        ")f1b61F2REOC",
        "Lz21E5as89hA",
        "abc123",
        "#EyBz6WQ!8K(",
        "a@L(7VZZ&olQ",
        "password",
        "rb)0(&xE*^zF",
        "Vs2$u96FwoAu",
        "password",
        "uLLaULycq*#P",
        "password",
        "9jFNZ4wY4s13",
        "D8Phy454aVDQ",
        "abc123",
        "q5DrBdfueIuL",
        "abc123",
        "qwerty",
        "password",
        "qwerty",
        "QTgs*G4wXm#k",
        "#Z&n)#YjFQqt",
        "BD6B2gcdUgB6",
        "!jQWd2KsP6H)",
        "7%&9X9H%*7WU",
        "rirk!RnUDK4A",
        "abc123",
        "kZ2gGm9)nh@Q",
        "TYZ)Ox4iE!*$",
        "Azs#PKnEULeF",
        "v$@m##D*A^G3",
        "wGPi@E0IptMG",
        "qwerty",
        "Xly4vNxxwDsk",
        "hFPZ5jOWUFO2",
        "abc123",
        "1qoQ)1WTpAro",
        "123abc",
        "123abc",
        "A5sC3Q(#pvwS",
        "123abc",
        "password",
        "g#Zmjy1jkq70",
        "qwerty",
        "password",
        "password",
        "Zw7A9g0nJxsI",
        "mJDUw8djZjja",
        "q%&WSogb!E!h",
        "^XVBNQFG9F8N",
        "HrZhqPLoikNZ",
        "Lm#szKuT#C*d",
        "!qeSYh8wfgIK",
        "abc123",
        "abc123",
        "123abc",
        "hUa0L($HXeU5",
        "a&Gn8vlcZQWT",
        "$zF7AODz0Ppg",
        "12345",
        "Zec0chW9Jhme",
        "v^3!ZxaH^&W&",
        "Q8%KiLNxKO&*",
        "qwerty",
        "123abc",
        "dCzm9jnHA4gH",
        "abc123",
        "password",
        "Dn5d^CI%y4oy",
        "(&#MxEd2E!sX",
        "abc123",
        "uB1&br#HhZxi",
        "password",
        "password",
        "ci(th@gLl1^V",
        "qwerty",
        "s2GmKg84jBDD",
        "password",
        "qwerty",
        "DQS$78dLDIBI",
        "5B*a8O)VEb*$",
        "n9DfqMvOsnx^",
        "qwerty",
        "LM12Os%L3BAm",
        "Iqo5xzDRqWdw",
        "password",
        "qrCQY!#uP(lI",
        "cF#!q&MEcnEG",
        "@$fA)BY*g7^*",
        "abc123",
        "password",
        "zp9$r5duiHUM",
        "00Z%g8leDppG",
        "7q^XIb3K^mmO",
        "password",
        "123abc",
        "password",
        "dOJCf3KR48c*",
        "FdTTUZQN6raa",
        "c4RreAD1C)s*",
        "abc123",
        "o4sg*T5YJlwa",
        "QNszeg!2MvQj",
        "qwerty",
        "abc123",
        "qwerty",
        "password",
        "bXOE$^v&rjxq",
        "123abc",
        "qwerty",
        "password",
        "123abc",
        "abc123",
        "abc123",
        "vlLSDn6kK%l$",
        "123abc",
        "xKbuuHw7vLaf",
        "123abc",
        "iL*6E8hgMipn",
        "abc123",
        "abc123",
        "nF($(aWFNKLn",
        "k^ZLpiPp%Fdx",
        "abc123",
        "qwerty",
        "&n$Zf!bP1!)M",
        "qwerty",
        "Oa3GU2HIP2P#",
        "password",
        "F*08*8hjy@oG",
        "qwerty",
        "SGKHIp)wVDlK",
        "l90$I8wvpmxq",
        "JcxVHa5XBN69",
        "eD$xom&RiVhL",
        "WO3K0P6NL6Gb",
        "abc123",
        "password",
        "abc123",
        "password",
        "qwerty",
        "97NqHQjqpKiu",
        "qwerty",
        "mdVZ7weWKc3)",
        "AI44(LY1Nt#3",
        "qwerty",
        "AnotherStrongPass2@",
        "9TEjd)^ffFpb",
        "MSkc9x6*DzQr",
        "spx75ae0n1h7",
        "password",
        "&PlaPsoq1qVP",
        "password",
        "xH1q()atCoLP",
        "123abc",
        "QG1L#6s&1qZT",
        "abc123",
        "abc123",
        "Zv6CgGzh$cnV",
        "password",
        "&jXYm@K#Jzfy",
        "5n1Z3XOjC97t",
        "!Hbycdyax5^s",
        "qwerty",
        "0%E#Iv@SDBwf",
        "NdbHyegGz%D9",
        "abc123",
        "abc123",
        "qwerty",
        "password",
        "abc123",
        "3B%ZFLjZpw5$",
        "kiGgKM*9NChQ",
        "password",
        "lLrQqPOBLhrZ",
        "qwerty",
        "qwerty",
        "abc123",
        "qwerty",
        "123abc",
        "TCOZaYECWDen",
        "qwerty",
        "bt*iGQi^xBXD",
        "abc123",
        "123abc",
        "123abc",
        "A0OR02M&5vzv",
        "123abc",
        "2j(mv6&bOn&W",
        "QEjlcl@Ef!kl",
        "123abc",
        "iL8$zNpod&v^",
        "password",
        "abc123",
        "password",
        "NtSs*pW@oecu",
        "123abc",
        "XyNZrPS@H&Rr",
        "abc123",
        "qwerty",
        "dfvf5@p*xx7$",
        "123abc",
        "(FgZ8LkcokXs",
        "password",
        "qwerty",
        "qwerty",
        "pql84ECaPcsU",
        "password",
        "abc123",
        "Hp)vR1)vF9iZ",
        "92Z^uO0zLbzY",
        "abc123",
        "password",
        "abc123",
        "3Ddy7FSOHb(8",
        "oQK6lN3fZhpn",
        "Lh0KXq^vfa@J",
        "l&gLClwUL3RO",
        "password",
        "VZzXT3)Dndog",
        "HzA)zMXdXe%v",
        "Hh9o1SrXXTup",
        "%CqHibUSvhs%",
        "*BdVU$GAs8B8",
        "password",
        "0GSJ@lZ7*Y#l",
        "OnU0FygvLlOl",
        "password",
        "abc123",
        "DEkO%XtzrGIx",
        "#Og$!URXHWgp",
        "AtWVh&cGteZc",
        "j0hcGlT60AB7",
        "123abc",
        "password",
        "YDg6aZAf3d!X",
        "j8jcKA52lN6W",
        "KiUt#1%bE(r)",
        "e8YgtwWlwtM&",
        "qwerty",
        "Zla&kF3HjQWh",
        "qwerty",
        "NE9sXpTB%7NK",
        "&IVvB5cV1151",
        "^yna5z!a)r5I",
        "qwerty",
        "abc123",
        "123abc",
        "abc123",
        "123abc",
        "abc123",
        "Xw0NXU^yYIpw",
        "4ntNqU)5Y0)8",
        "rRphkktUJx3C",
        "abc123",
        "8rf33mc9H@%3",
        "password",
        "k)t*jFMpg!0C",
        "abc123",
        "qNs6coqyc5fx",
        "zej7uV%I(RwZ",
        "&X^43Se*X*Um",
        "password",
        "27MILZIEV#7r",
        "fMcr1Mb7aEE8",
        "q3Z!1%#Y5^vM",
        "j3gc7B0a2F)X",
        "dpGpju4X3HhD",
        "123abc",
        "*HmTfQEOaDvL",
        "password",
        "t26VsQdR&wf4",
        "123abc",
        "0OgZMuHk97YC",
        "MjuzLSGC1))0",
        "K#qP!cgS2zm)",
        "6q#dFuQsyzuQ",
        "iYzTcbRIysLK",
        "Vt*Qao4F4puw",
        "abc123",
        "123abc",
        "1A35ZH$T(Z!@",
        "123abc",
        "PmXpryHNhUUU",
        "#Th#Y!XqCGPE",
        "T7skz1k(zN8R",
        "0N3jDqch^IA!",
        "@lim38PdimP3",
        "abc123",
        "dEFQqpy^nGbC",
        "qwerty",
        "s3&CYvQILS9L",
        "123abc",
        "Rx6L(ha2q5!j",
        "m6CjcPwMf2tq",
        "123abc",
        "123abc",
        "password",
        "password",
        "password",
        "g5UxD!NR$Ko5",
        "zJuVqRX%AC5K",
        "password",
        "hTGiWTdPNaU3",
        "eb&Ddt#MNR^W",
        "899jeGF2UEdu",
        "p(orLOz!7x*m",
        "*RZmWpd8xZ*&",
        "4TA2FTo38tiD",
        "RgnY3x#W(*UZ",
        "sDM&UX$M86%b",
        "123abc",
        "mg56YsJRPncK",
        "123abc",
        "password",
        "Dvs&oLY8h%jc",
        "password",
        "qwerty",
        "pW95oL%LLg7G",
        "e&gtgL&81FsW",
        "abc123",
        "g1NPJ)2@HcpA",
        "*efz&%rIN1jB",
        "t*lSZu^y9bbr",
        "abc123",
        "abc123",
        "S(Te@ec^cf59",
        "YIGLUH9bd8ma",
        "123abc",
        "1aFpi^UdyE$F",
        "Om1&3^l8w2oC",
        "qwerty",
        "abc123",
        "abc123",
        "qwerty",
        "bDzft%aIJ4uU",
        "qM)S!*ZS^MqS",
        "123abc",
        "123abc",
        "ov6ttHeMPOs4",
        "abc123",
        "s#jLsVS@1J&8",
        "qwerty",
        "u@tyO9S9^gAi",
        "abc123",
        "Nv$2L0wvpA7J",
        "^Fjyer9O$ASr",
        "qwerty",
        "abc123",
        "n7q@ClZxr2qM",
        "(rNOBmJ&v%ol",
        "JkyDPh2TdXe2",
        "abc123",
        "2Db6oYdct6tD",
        "password",
        "password",
        "R5fnRsME2c)A",
        ")$N^D5w!42A*",
        "123abc",
        "FXd2N@y^5cJr",
        "DhY7(NW$yeAu",
        "password",
        "password",
        "qwerty",
        "password",
        "x2U#N70MZqEz",
        "qwerty",
        "123abc",
        "Q4F#cob)*v)y",
        "123abc",
        "DUW8BL1a6uEN",
        "123abc",
        "password",
        "password",
        "qwerty",
        "8K$^wwxY#VRm",
        "%GYmRt*ieC(*",
        "pc0Z(4hoJWi2",
        "6Un9lTf&7D5R",
        "123abc",
        "abc123",
        "qwerty",
        "vZmW&)vQj*LD",
        "qwerty",
        "abc123",
        "L0cU@v4AQD5M",
        "SkKg3)J@9Ln1",
        "rvQ8O65Sxoxu",
        "qwerty",
        "password",
        "gk8XcquMmZzc",
        "123abc",
        "qwerty",
        "123abc",
        "TgirXeRV4q6m",
        "OQuaxESN8cdV",
        "abc123",
        "123abc",
        "cboSgG9V!vPH",
        "ee^jn3D!xFTt",
        "qwerty",
        "qwerty",
        "Ks^ZYpdwNMvY",
        "abc123",
        "q6G@4q8@dZjr",
        "dRtL%Gqp60QN",
        "password",
        "qwerty",
        "123abc",
        "p7Wd2pPx@04G",
        "123abc",
        "RjKb^fEPPi9t",
        "qwerty",
        "123abc",
        "Qy!1&YiRl6vX",
        "qwerty",
        "Jz2b(I#gMF7I",
        "qwerty",
        "password",
        "0Wj1@jg1hAjD",
        "5hq1huqz9giB",
        "password",
        "password",
        "u)*%S)Ytsy($",
        "123abc",
        "123abc",
        "abc123",
        "123abc",
        "oSV7Fsm0Cn3f",
        "123abc",
        "^GYCmRBXf9zT",
        "qwerty",
        "password",
        "z20zkmSFyZo$",
        "123abc",
        "abc123",
        "qwerty",
        "xxEBmkWU2MEq",
        "YD0&2RcmyTtg",
        "123abc",
        "password",
        "Kemj%WZNls0b",
        "qwerty",
        "123abc",
        "J(VdlBF#w0aK",
        "abc123",
        "123abc",
        "61ahUrlQjJ!S",
        "qwerty",
        "qwerty",
        "password",
        "password",
        "r)%uEkMz0PWG",
        "password",
        "qwerty",
        "PDlgGGo&@qoe",
        "25FOJ3o4VQwS",
        "password",
        "QIJ6w)Uy4(wF",
        "password",
        "pc*52ovvfzWK",
        "2XeaF(uk9nP2",
        "Sf%dsswqU!Xa",
        "password",
        "An$)O^8L866c",
        "abc123",
        "password",
        "qwerty",
        "LJWUWsfK15Wb",
        "!4z&%nEybE*g",
        "(ompNfam1fMZ",
        "4OBoyBY^I#@r",
        "password",
        "password",
        "KM&ax5SWOWsg",
        "qwerty",
        "password",
        "qwerty",
        "ENoi!FvvmOgT",
        "123abc",
        "qwerty",
        "fxANB5W6icBy",
        "qwerty",
        "password",
        "abc123",
        "qwerty",
        "qwerty",
        "k3qG3OFFMU45",
        "qwerty",
        "123abc",
        "abc123",
        "O8Bsor1JxnOx",
        "!ex&fZPM8ptm",
        "@s0m&Z$VgMPf",
        "XaCOR4Mms8&9",
        "123abc",
        "m$eZuHS31zpI",
        "password",
        "olIB5ejGu7N#",
        "abc123",
        "i&ezv17vRPEn",
        "qwerty",
        "password",
        "123abc",
        "abc123",
        "IqFmNAjv4UfV",
        "password",
        "123abc",
        "vo$^fWmc0qb(",
        "1AKLDm)OxhkL",
        "password",
        "qwerty",
        "123abc",
        "123abc",
        "abc123",
        "uJIn$miWrf7H",
        "H3ylq#2&ncnN",
        "qwerty",
        "password",
        "495Zd1z1ppoB",
        "XEfa1x%MfWxf",
        "abc123",
        "8ZIZJ%!kQ5zq",
        "123abc",
        "J7MgF8gPR4gp",
        "cHa6f^a0gB!K",
        "gD0pK*TdR6B&",
        "123abc",
        "123abc",
        "abc123",
        "*JzeoS3Lf#ao",
        "password",
        "abc123",
        "password",
        "MOY4rT6D@ST4",
        "StrongPass1!",
        "qwerty",
        "vJcah6qI9z@I",
        "y#v8#2Ywz8$5",
        "0ur^R2#qkZDk",
        "ODv5oqn^UyUB",
        "gBtW2v!8Qzcw",
        "E(SzG4ExsS)4",
        "mOCBjKe0i*!H",
        "rZ7ULC!Pc9L#",
        "qwerty",
        "abc123",
        "abc123",
        "PydNq4Z7RJY(",
        "#6JKnh#(tJVJ",
        "9XyswCyqXvAM",
        "8f#zJe#0NbNv",
        "password",
        "123abc",
        "hh5%YyN$0u8N",
        "ZGTZU9Kfx8hp",
        "jLEjAI1KTobt",
        "f80BE#p&YyZ5",
        "TxqxYJ&Wz&ss",
        "123abc",
        "qwerty",
        "k)eq7V1A8kZ^",
        "T4Pkd43cC23A",
        "45GIGhg4Pqf^",
        "kxx7kT6bDb#F",
        "password",
        "123abc",
        "abc123",
        "123abc",
        "abc123",
        "H#iaW(!^%U95",
        "E0dSSFqBO3ak",
        "password",
        "GcModA7uQy2K",
        "rwdbfva)z)$v",
        "password",
        "f3W^&L&53(q7",
        "abc123",
        "password",
        "qwerty",
        "qwerty",
        "^Aj@^nS&2IF7",
        "^QBFYnvqbepp",
        "yw&AlR38Z$3k",
        "123abc",
        "abc123",
        "jper)@rjuiYA",
        "password",
        "V^C!zkf8P(bf",
        "qwerty",
        "123abc",
        "abc123",
        "lfB)NhNIGhQ7",
        "qwerty",
        "123abc",
        "password",
        "ERG@$*Qh!SBr",
        "123abc",
        "!oWlzXu8wAUs",
        "rAaM6%kzce^M",
        "!6^EXUWh$IEY",
        "password",
        "abc123",
        "abc123",
        "18N71OFnzDPC",
        "Sf)#BAufm#S)",
        "AEfl%h!6O(bO",
        "abc123",
        "qwerty",
        "MN4)TsKLkLQc",
        "f#9!31hhkE)5",
        "abc123",
        "abc123",
        "abc123",
        "password",
        "27FvFzNm7^2M",
        "81cB&MYPO!qZ",
        "hZDiL8FGwFT3",
        "Q(OF3zKWw)R%",
        "ZSY6W@bfIP%R",
        "123abc",
        "abc123",
        "1DVG!cCIlp9G",
        "5^MvfAmrEIu9",
        "nc2AcYI9w!&e",
        "password",
        "password",
        "tEa03VpcIOj6",
        "y^s9%hlY0RHt",
        "123abc",
        "R4#EGCJTTdg5",
        "abc123",
        "JL1M60C&BF^^",
        "123abc",
        "rnY&*il55y4J",
        "9WZJq41B%Kag",
        "UdQCZiy6lO4O",
        "TU0GCTBpc1MA",
        "abc123",
        "qwerty",
        "Gno#DK1tTn%5",
        "LiBr0*E2oF6T",
        "VuL(e7Q(Z3T2",
        "qwerty",
        "abc123",
        "cauuZwEz*FKk",
        "qwerty",
        "123abc",
        "SsSnU9hQJ0J9",
        "kjeArrbd0Zxx",
        "qwerty",
        "PflJxP*owAQ4",
        "abc123",
        "yVkq6K61erg5",
        "0jcN^LO3v8v#",
        "password",
        "uFdsr54lPY2O",
        "abc123",
        "#21mqwF3Awx6",
        "qwerty",
        "7Wr2LdY$^fNW",
        "123abc",
        "U0RUNy69ZuG8",
        "qEPAYjYsGI*S",
        "UnK0IR5pHZSr",
        "%x*yqEJjqPlt",
        "abc123",
        "weak",
        "qwerty",
        "123abc",
        "x7xit&Xx89j4",
        "d6wJuOVC7yDY",
        "HN7#w*FYH^IS",
        "scayfyEcldH4",
        "1q30mUFgf65x",
        "password",
        "J9IYK&RgtLqp",
        "J*@HF^ssqF$I",
        "qwerty",
        "qwerty",
        "fc39rKJ6OOvi",
        "abc123",
        "123abc",
        "^)&9QsqTC0R)",
        "WXOc19ojM4Zo",
        "HPzcs(R5h*Dp",
        "riS2!aC@1JDM",
        "lbllX88*jH)A",
        "LkjrW1j*@DUi",
        "oyGe304f5iHE",
        "abc123",
        "abc123",
        "qwerty",
        "WOq8XvwVx9Y9",
        "6tXpK%b3M^dn",
        "123abc",
        "password",
        "password",
        "abc123",
        "4Fg8WH#Fs7ZQ",
        "123abc",
        "!RGe7qq4pmMc",
        "kIxetvp$t6$Q",
        "qwerty",
        "password",
        "qwerty",
        "abc123",
        "password",
        "qwerty",
        "seh9hCxX^@En",
        "E%AG*WYQhBpK",
        "abc123",
        "N1@7VYro@J$B",
        "abc123",
        "5gm7)MxC2PYv",
        "qwerty",
        "rqxv5axh@Pp0",
        "Fian^#27gZ%a",
        "&DgJFFe7@tBV",
        "abc123",
        "qwerty",
        "password",
        "qgurvmdN36Mh",
        "password",
        "7sgN%#jeO&gy",
        "123abc",
        "123abc",
        "HrF2&s@Ohu&T",
        "abc123",
        "password",
        "Gn%IZ2dPAQse",
        "abc123",
        "123abc",
        "password",
        "cu(1j@jB91xd",
        "zz49VXlvKbxF",
        "password",
        "123abc",
        "zZE(oD46)b^2",
        "abc123",
        "qwerty",
        "123abc",
        "wi3ofYB*ao8%",
        "password",
        "qwerty",
        "qwerty",
        "nG7R#gYykMOd",
        "nvI9#kv8*Gch",
        "jC%ZMUnE9kFH",
        "3q#52Zn4s%9L",
        "ZaW8O$Ct6h9A",
        "abc123",
        "123abc",
        "SC9Wra5@766L",
        "qwerty",
        "123abc",
        "123abc",
        "En$FZZ2mwLTp",
        "W%!*Sl#UEXd^",
        "izNfkEtvx7hX",
        "LOvPmNt1ki8T",
        "123abc",
        "qwerty",
        "qwerty",
        "1aG&AlZ*JpS$",
        "qwerty",
        "GsxRzOe82oR%",
        "K#nFfy*Xd1es",
        "qwerty",
        "password",
        "abc123",
        "qwerty",
        "(#rr64Pj!Uz&",
        "EX5qz4v21qgf",
        "hiI3S*nTy7$O",
        "password",
        "BQHXsJ!5TR9^",
        "^*g)QUHcX$gx",
        "VQ7d%PiRyU*H",
        "gas^ZvRNAg1B",
        "password",
        "ZE1Q60@1UJx@",
        "qwerty",
        "123abc",
        "password",
        "0K@$ypj6KTjW",
        "123abc",
        "%yfBPh2e)gwN",
        "AP7USBma)l96",
        "FLGti8UH8FOt",
        "VQtao7B9hGO0",
        "abc123",
        "123abc",
        "X!7Fp^ubnwCP",
        "password",
        "P(&Cwpv7D4&^",
        "XZH11bAeAOLj",
        "SeWWcgUQhPVx",
        "qwerty",
        "do8q18HK!CvS",
        "zi58^jlkwxfH",
        "#mj@9u!h^4Km",
        "%AxBlGD4e8pP",
        "qwerty",
        "abc123",
        "qwerty",
        "password",
        "WB6JGf19FS)I",
        "abc123",
        "123abc",
        "^SXi9Hsj)2UB",
        "NJ6dBoz%wgrU",
        "yd7l^it$wfX%",
        "123abc",
        "password",
        "123abc",
        "Hp!0^0S2fDaV",
        "r@hQAeul#A18",
        "qwerty",
        "I5$1PX@qdgT7",
        "qwerty",
        "123abc",
        ")v4li(Dfk&lv",
        "qwerty",
        "PU0TpCJunJ$n",
        "password",
        "123abc",
        "*&LFU*1o9!cG",
        "S^&EsoWpcIaz",
        "CnpHF^aMC8jd",
        "password",
        "123abc",
        "YQ$QYZ%!7JoD",
        "0vSGQ6uj5ngb",
        "tSVK(!&%kU(L",
        "abc123",
        "7Fy8Y&LB)POh",
        "zjMK(@TN7%Y6",
        "kJZgmWoyXc7U",
        "abc123",
        "password",
        "qwerty",
        "xbNMfpx37ORi",
        "rZENu!KT&!sx",
        "zvhU9y6Ihk!a",
        "RS)DPHDYZVMT",
        "zC!ndEtx2%A@",
        "password",
        "123abc",
        "abc123",
        "MUPqpmGtt2!F",
        "3zyeevm064yL",
        "123abc",
        "dA@Fgosnig9%",
        "X#VBubO)m3pb",
        "abc123",
        "DwgShOa!VQkO",
        "oybxP30eb8Ts",
        "oBL@pKwJ$9Qx",
        "%YS0qW!5gN4d",
        "aM1!N)!NpOq0",
        "OdKAa19!EUf*",
    ]

    res = validate_passwords(pwd)
    assert isinstance(res, list)
    assert res.count(True) == 324
    assert res.count(False) == 676


@pytest.mark.timeout(0.3)
def test_extract_host_from_url_1():
    urls = [
        "https://www.example.com/page",
        "http://subdomain.example.org/",
        "http://www.media.mit.edu/",
    ]
    res = extract_host_from_url(urls)
    assert isinstance(res, list)
    assert res == ["www.example.com", "subdomain.example.org", "www.media.mit.edu"]


@pytest.mark.timeout(0.3)
def test_extract_host_from_url_2():
    urls = []
    res = extract_host_from_url(urls)
    assert isinstance(res, list)
    assert res == []


@pytest.mark.timeout(0.3)
def test_extract_host_from_url_3():
    urls = [
        "https://usc.edu/SBu5pf8Nw",
        "https://transport.ucla.edu/Z?Uui4",
        "https://tesla.com/fg1kd",
        "https://www.amazon.com/jLquv?26uVT",
        "https://myviterbi.usc.edu/0cE",
        "https://www.cisco.com/wr?19uczNwIs0",
        "https://my.usc.edu/OHqw",
        "https://www.amazon.com/Z?B9hOa",
        "https://github.com/n4uv",
        "https://tesla.com/ro?I",
        "https://github.com/k",
        "https://cisco.webex.com/ZLU2BRwC?HS5pst",
        "https://transport.ucla.edu/m",
        "https://github.com/DwjdjF",
        "https://myviterbi.usc.edu/w",
    ]

    res = extract_host_from_url(urls)
    assert isinstance(res, list)
    assert res == [
        "usc.edu",
        "transport.ucla.edu",
        "tesla.com",
        "www.amazon.com",
        "myviterbi.usc.edu",
        "www.cisco.com",
        "my.usc.edu",
        "www.amazon.com",
        "github.com",
        "tesla.com",
        "github.com",
        "cisco.webex.com",
        "transport.ucla.edu",
        "github.com",
        "myviterbi.usc.edu",
    ]


@pytest.mark.timeout(0.3)
def test_extract_host_from_url_4():
    urls = [
        "https://tesla.com//SRSAM6sm?OCsrgEfK",
        "https://myviterbi.usc.edu/CvvQ?kizq",
        "https://www.cisco.com/G?VvudPcnimH",
        "https://my.usc.edu/uWk6rJm?g",
        "https://my.usc.edu/10rlJ?OmxCTSj2d",
        "https://www.cisco.com/G?jPNT",
        "https://www.annenberg.usc.edu/N?HWb",
        "https://chat.openai.com/fQWVetkg",
        "https://myviterbi.usc.edu/upi?c6IYn1SK",
        "https://usc.edu/BDkwIpE",
        "https://www.annenberg.usc.edu/WSQ?jUxYv",
        "https://usc.edu/LkP20?KcVk",
        "https://www.amazon.com/APF2",
        "https://github.com/ULv?ELTQ3FT",
        "https://my.usc.edu/STnUaIo6",
        "https://usc.edu/V",
        "https://github.com/WPG9tnh38?6LO22",
        "https://www.annenberg.usc.edu/3WJOT0X?ayS",
        "https://my.usc.edu/Mo5mu",
        "https://www.cisco.com/cET",
        "https://www.cisco.com/BDcMeAj",
        "https://openai.com/MoSVDEbRiQ?5I",
        "https://myviterbi.usc.edu/JNpx2r5PQY",
        "https://myviterbi.usc.edu/vcHR2ekH4",
        "https://www.cisco.com/cd?fMDH3Po",
        "https://github.com/5U3VD5pj?31Ej4LfY",
        "https://myviterbi.usc.edu/KRWfxsDxxv?hnNkCkbq",
        "https://cisco.webex.com/ptwVq?07co3B7",
        "https://github.com/J3AfwYo?uSZuYcJ",
        "https://myviterbi.usc.edu/fuLtDOV?mUH1iHMp",
        "https://www.amazon.com/Q",
        "https://transport.ucla.edu/caxqxqit",
        "https://github.com/zR13Fbj?L",
        "https://www.amazon.com/rWVs",
        "https://www.cisco.com/YWgK",
    ]

    res = extract_host_from_url(urls)
    assert isinstance(res, list)
    assert res == [
        "tesla.com",
        "myviterbi.usc.edu",
        "www.cisco.com",
        "my.usc.edu",
        "my.usc.edu",
        "www.cisco.com",
        "www.annenberg.usc.edu",
        "chat.openai.com",
        "myviterbi.usc.edu",
        "usc.edu",
        "www.annenberg.usc.edu",
        "usc.edu",
        "www.amazon.com",
        "github.com",
        "my.usc.edu",
        "usc.edu",
        "github.com",
        "www.annenberg.usc.edu",
        "my.usc.edu",
        "www.cisco.com",
        "www.cisco.com",
        "openai.com",
        "myviterbi.usc.edu",
        "myviterbi.usc.edu",
        "www.cisco.com",
        "github.com",
        "myviterbi.usc.edu",
        "cisco.webex.com",
        "github.com",
        "myviterbi.usc.edu",
        "www.amazon.com",
        "transport.ucla.edu",
        "github.com",
        "www.amazon.com",
        "www.cisco.com",
    ]


@pytest.mark.timeout(0.3)
def test_extract_host_from_url_5():
    urls = [
        "https://tesla.com//SRSAM6sm?OCsrgEfK",
        "https://myviterbi.usc.edu/CvvQ?kizq",
        "https://www.cisco.com/G?VvudPcnimH",
        "https://my.usc.edu/uWk6rJm?g",
        "https://my.usc.edu/10rlJ?OmxCTSj2d",
        "https://www.cisco.com/G?jPNT",
        "https://www.annenberg.usc.edu/N?HWb",
        "https://chat.openai.com/fQWVetkg",
        "https://myviterbi.usc.edu/upi?c6IYn1SK",
        "https://usc.edu/BDkwIpE",
        "https://www.annenberg.usc.edu/WSQ?jUxYv",
        "https://usc.edu/LkP20?KcVk",
        "https://www.amazon.com/APF2",
        "https://github.com/ULv?ELTQ3FT",
        "https://my.usc.edu/STnUaIo6",
        "https://usc.edu/V",
        "https://github.com/WPG9tnh38?6LO22",
        "https://www.annenberg.usc.edu/3WJOT0X?ayS",
        "https://my.usc.edu/Mo5mu",
        "https://www.cisco.com/cET",
        "https://www.cisco.com/BDcMeAj",
        "https://openai.com/MoSVDEbRiQ?5I",
        "https://myviterbi.usc.edu/JNpx2r5PQY",
        "https://myviterbi.usc.edu/vcHR2ekH4",
        "https://www.cisco.com/cd?fMDH3Po",
        "https://github.com/5U3VD5pj?31Ej4LfY",
        "https://myviterbi.usc.edu/KRWfxsDxxv?hnNkCkbq",
        "https://cisco.webex.com/ptwVq?07co3B7",
        "https://github.com/J3AfwYo?uSZuYcJ",
        "https://myviterbi.usc.edu/fuLtDOV?mUH1iHMp",
        "https://www.amazon.com/Q",
        "https://transport.ucla.edu/caxqxqit",
        "https://github.com/zR13Fbj?L",
        "https://www.amazon.com/rWVs",
        "https://www.cisco.com/YWgK",
    ]
    res = extract_host_from_url(urls)
    assert isinstance(res, list)
    assert res == [
        "tesla.com",
        "myviterbi.usc.edu",
        "www.cisco.com",
        "my.usc.edu",
        "my.usc.edu",
        "www.cisco.com",
        "www.annenberg.usc.edu",
        "chat.openai.com",
        "myviterbi.usc.edu",
        "usc.edu",
        "www.annenberg.usc.edu",
        "usc.edu",
        "www.amazon.com",
        "github.com",
        "my.usc.edu",
        "usc.edu",
        "github.com",
        "www.annenberg.usc.edu",
        "my.usc.edu",
        "www.cisco.com",
        "www.cisco.com",
        "openai.com",
        "myviterbi.usc.edu",
        "myviterbi.usc.edu",
        "www.cisco.com",
        "github.com",
        "myviterbi.usc.edu",
        "cisco.webex.com",
        "github.com",
        "myviterbi.usc.edu",
        "www.amazon.com",
        "transport.ucla.edu",
        "github.com",
        "www.amazon.com",
        "www.cisco.com",
    ]
