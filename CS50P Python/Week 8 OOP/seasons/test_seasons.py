from seasons import minutes


def test_date():
    assert minutes(10477) == "Fifteen million, eighty-six thousand, eight hundred eighty minutes"
    assert minutes(365) == "Five hundred twenty-five thousand, six hundred minutes"