from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: int, quantity: int, number_of_sim: int) -> None:
        super().__init__(name, price, quantity)
        self.__number_of_sim: int = self.check_number_of_sim(number_of_sim)

    def __str__(self) -> str:
        """
        Выводит сообщение о модели телефлна
        """
        return f"{self.name}"

    def __repr__(self) -> str:
        """
        Выводит сообщение о классе и свойствах  класса
        """
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.__number_of_sim})"

    @property
    def number_of_sim(self) -> int:
        """
        Геттер для number_of_sim
        """
        return self.__number_of_sim

    @staticmethod
    def check_number_of_sim(number_of_sim):
        if number_of_sim <= 0 or not isinstance(number_of_sim, int):
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля")
        return number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        self.__number_of_sim = self.check_number_of_sim(value)
