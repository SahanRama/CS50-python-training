from bank import value

def main():
    test_value_for_hello()
    test_value_for_h_word()
    test_value_for_non_h_words()
    test_value_for_special_charactors()

def test_value_for_hello():
    assert value("HELLO") == 0
    assert value("hello") == 0

def test_value_for_h_word():
    assert value("how are you") == 20
    assert value("Howdy?") == 20

def test_value_for_non_h_words():
    assert value("whats up?") == 100
    assert value("Good day to you") == 100

def test_value_for_special_charactors():
    assert value(")(*&^%$#@)") == 100


if __name__ == "__main__":
    main()
