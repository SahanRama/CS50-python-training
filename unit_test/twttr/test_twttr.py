from twttr import shorten


def main():
    test_words_without_vowel()
    test_words_with_vowel()


def test_words_without_vowel():
    assert shorten("Flyby") == "Flyby"
    assert shorten("crypt") == "crypt"


def test_words_with_vowel():
    assert shorten("Kaushalya") == "Kshly"
    assert shorten("sahan") == "shn"


def test_omitting_numbers():
    assert shorten("CS50") == "CS50"


def test_printing_in_uppercase():
    assert shorten("TORONTO") == "TRNT"


def test_omitting_punctuation():
    assert shorten("What's your name?") == "Wht's yr nm?"


if __name__ == "__main__":
    main()
