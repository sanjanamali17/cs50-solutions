from plates import is_valid


def test_length():
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False


def test_start_letters():
    assert is_valid("CS50") == True
    assert is_valid("50CS") == False
    assert is_valid("C1") == False


def test_numbers_position():
    assert is_valid("AAA111") == True
    assert is_valid("AA11A") == False


def test_leading_zero():
    assert is_valid("CS05") == False
    assert is_valid("CS50") == True


def test_characters():
    assert is_valid("PI3.14") == False
    assert is_valid("HELLO!") == False
