from pathlib import Path

import pytest

from src.exceptions import InstantiateCSVError
from src.item import Item
from src.settings import BROKEN_ITEMS_CSV_PATH
from tests.test_phone import class_test_phone

ROOT_PATH = Path(__file__).parent.parent
SCR_PATH = ROOT_PATH.joinpath("src", "items.csv")


@pytest.fixture()
def class_test_item():
    return Item("Смартфон", 10000, 2)


def test_calculate_total_price(class_test_item):
    assert class_test_item.calculate_total_price() == 20000


def test_apply_discount(class_test_item):
    assert class_test_item.price == 10000
    class_test_item.pay_rate = 0.5
    class_test_item.apply_discount()
    assert class_test_item.price == 5000


def test_string_to_number(class_test_item):
    assert class_test_item.string_to_number("7.5") == 7
    assert class_test_item.string_to_number("7") == 7
    assert class_test_item.string_to_number(5) == 5


def test_name(class_test_item):
    assert class_test_item.name == "Смартфон"
    class_test_item.name = "СмартфонХХХХХХХХХХХХХ"
    assert class_test_item.name == "СмартфонХХ"


def test_instantiate_from_csv(class_test_item):
    class_test_item.instantiate_from_csv(SCR_PATH)
    assert len(Item.all) == 5


def test_repr(class_test_item):
    assert repr(class_test_item) == "Item('Смартфон', 10000, 2)"


def test_str(class_test_item):
    assert str(class_test_item) == 'Смартфон'


def test_add(class_test_item, class_test_phone):
    assert class_test_item + class_test_phone == 7


def test_add_failed(class_test_item):
    with pytest.raises(ValueError):
        class_test_item + 10


def test_file_not_found_error(class_test_item):
    with pytest.raises(FileNotFoundError):
        # class_test_item.instantiate_from_csv("")
        assert class_test_item.instantiate_from_csv('') == "Отсутствует файл item.csv"
    # with pytest.raises(InstantiateCSVError):
    #     assert class_test_item.instantiate_from_csv(BROKEN_ITEMS_CSV_PATH) == "Файл item.csv поврежден"


def test_key_error(class_test_item):
    with pytest.raises(InstantiateCSVError):
        # class_test_item.instantiate_from_csv(BROKEN_ITEMS_CSV_PATH)
        assert class_test_item.instantiate_from_csv(BROKEN_ITEMS_CSV_PATH) == "Файл item.csv поврежден"