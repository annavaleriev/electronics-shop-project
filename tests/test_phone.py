import pytest

from src.phone import Phone

# # смартфон iPhone 14, цена 120_000, количество товара 5, симкарт 2
# phone1 = Phone("iPhone 14", 120_000, 5, 2)
# assert str(phone1) == 'iPhone 14'
# assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"
#
# def test_repr(class_test_item):
#     assert repr(class_test_item) == "Item('Смартфон', 10000, 2)"
#
#
# def test_str(class_test_item):
#     assert str(class_test_item) == 'Смартфон'
#

@pytest.fixture()
def class_test_phone():
    return Phone("iPhone 14", 120000, 5, 2)


def test_repr(class_test_phone):
    assert repr(class_test_phone) == "Phone('iPhone 14', 120000, 5, 2)"


def test_str(class_test_phone):
    assert str(class_test_phone) == "iPhone 14"


def test_number_of_sim(class_test_phone):
    assert class_test_phone.number_of_sim == 2
    if class_test_phone.number_of_sim == 0:
        assert class_test_phone.number_of_sim == "Количество физических SIM-карт должно быть целым числом больше нуля"
    if class_test_phone.number_of_sim == 1.2:
        assert class_test_phone.number_of_sim == "Количество физических SIM-карт должно быть целым числом больше нуля"
    if class_test_phone.number_of_sim == -5:
        assert class_test_phone.number_of_sim == "Количество физических SIM-карт должно быть целым числом больше нуля"




    # def number_of_sim(self, value):
    #     if value <= 0:
    #         raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля")
    #     else:
    #         self.__number_of_sim = value
    #
# phone1.number_of_sim = 0
#     # ValueError: Количество физических SIM-карт должно быть целым числом больше нуля.



