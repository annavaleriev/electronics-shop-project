import pytest

from src.keyboard import Keyboard


@pytest.fixture()
def class_test_keyboard():
    return Keyboard("Dark Project KD87A", 9600, 5)


def test_name_keyboard(class_test_keyboard):
    assert class_test_keyboard.name == "Dark Project KD87A"


def test_default_language(class_test_keyboard):
    assert class_test_keyboard.language == "EN"


def test_change_language_ru(class_test_keyboard):
    class_test_keyboard.change_lang()
    assert class_test_keyboard.language == "RU"


def test_change_language_en(class_test_keyboard):
    class_test_keyboard.change_lang()
    class_test_keyboard.change_lang()
    assert class_test_keyboard.language == "EN"


def test_test_change_language_other(class_test_keyboard):
    with pytest.raises(AttributeError):
        class_test_keyboard.language = "CH"
