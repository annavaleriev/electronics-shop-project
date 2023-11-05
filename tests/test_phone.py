import pytest

from src.phone import Phone


@pytest.fixture()
def class_test_phone():
    return Phone("iPhone 14", 120000, 5, 2)


def test_repr(class_test_phone):
    assert repr(class_test_phone) == "Phone('iPhone 14', 120000, 5, 2)"


def test_str(class_test_phone):
    assert str(class_test_phone) == "iPhone 14"


def test_number_of_sim(class_test_phone):
    with pytest.raises(ValueError):
        Phone("iPhone 14", 120000, 5, 0)
    with pytest.raises(ValueError):
        class_test_phone.number_of_sim = 0
    with pytest.raises(ValueError):
        class_test_phone.number_of_sim = 1.1


def test_check_number_of_sim(class_test_phone):
    assert class_test_phone.check_number_of_sim(1) == 1
    with pytest.raises(ValueError):
        class_test_phone.check_number_of_sim(1.1)
    with pytest.raises(ValueError):
        class_test_phone.check_number_of_sim(-1)
