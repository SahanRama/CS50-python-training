from plates import is_valid

def main():
    test_at_least_start_with_two_letters()
    test_plate_length()
    test_starting_number_validation()
    test_special_charactor_validation()


def test_at_least_start_with_two_letters():
    assert is_valid("CS50") == True
    assert is_valid("5020") == False
    assert is_valid("!@#") == False

def test_plate_length():
    assert is_valid("CS") == True
    assert is_valid("ABCD") == True
    assert is_valid("ABCDEF") == True
    assert is_valid("A") == False
    assert is_valid ("ABCDEFG") == False

def test_starting_number_validation():
    assert is_valid("ADD300") == True
    assert is_valid("CS05") == False
    assert is_valid("BOC22D") == False

def test_special_charactor_validation():
    assert is_valid("ADA BA") == False
    assert is_valid("ADA.BA") == False
    assert is_valid("ADA,BA") == False
    assert is_valid("ADA@BA") == False




if __name__ == "__main__":
    main()
