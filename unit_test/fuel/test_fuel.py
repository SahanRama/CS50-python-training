import pytest
from fuel import convert, gauge


def main():
    test_convert_persentage()
    test_convert_zero_devition_error()
    test_incorect_int_convert()


def test_convert_persentage():
    assert convert("25/50") == 50
    assert convert("0/200") == 0
    assert convert("3/4") == 75
    assert convert("4/4") == 100


def test_convert_zero_devition_error():
    with pytest.raises(ZeroDivisionError):
        convert("12/0")


def test_incorect_int_convert():
    with pytest.raises(ValueError):
        convert("cat/dog")


def test_raised_value_error():
    with pytest.raises(ValueError):
        convert("30/10")


def test_gauge_when_empty():
    assert gauge(0) == "E"
    assert gauge(1) == "E"


def test_gauge_when_full():
    assert gauge(99) == "F"
    assert gauge(100) == "F"


def test_gauge_when_percentage():
    assert gauge(50) == "50%"
    assert gauge(2) == "2%"
    assert gauge(98) == "98%"


def test_gauge_with_convert_values():
    assert gauge(convert("0/100")) == "E"
    assert gauge(convert("1/100")) == "E"
    assert gauge(convert("100/100")) == "F"
    assert gauge(convert("99/100")) == "F"
    assert gauge(convert("50/100")) == "50%"

if __name__ == "__main__":
    main()
