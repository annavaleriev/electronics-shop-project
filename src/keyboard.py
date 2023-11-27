from src.item import Item


class KeyboardMixin:

    __language = "EN"

    @property
    def language(self):
        """
        Геттер для language
        """
        return self.__language

    def change_lang(self):
        """
        Метод, который меняет язык клавиатуры
        """
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"


class Keyboard(KeyboardMixin, Item):
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
