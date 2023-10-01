import pytest
from src.item import Item


@pytest.fixture()
def class_test_item():
    return Item("Смартфон", 10000, 2)


def test_calculate_total_price(class_test_item):
    assert class_test_item.calculate_total_price() == 20000


def test_apply_discount(class_test_item):
    assert class_test_item.apply_discount() is None
