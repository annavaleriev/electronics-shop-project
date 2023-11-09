import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate: float = 1.0
    all: list = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """

        self.__name: str = name[:10]
        self.price: float = price
        self.quantity: int = quantity
        Item.all.append(self)

    def __repr__(self):
        """
        Выводит сообщение о классе и свойствах  класса
        """
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        """
        Выводит сообщение c названием товара
        """
        return f'{self.__name}'

    @property
    def name(self) -> str:
        """
        Геттер для name
        """
        return self.__name

    @name.setter
    def name(self, name) -> None:

        """
        Сеттер для name
        """
        self.__name = name[:10]

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, csv_file):
        """
        Инициализирует экземпляры класса из 'csv' файла.
        """
        cls.all.clear()
        with open(csv_file, encoding="windows-1251") as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row["name"]
                price = float(row["price"])
                amount = int(row["quantity"])
                cls(name, price, amount)

    @staticmethod
    def string_to_number(string):
        """
        Статический метод, возвращающий число из числа-строк
        """
        try:
            return int(float(string))
        except ValueError:
            raise ValueError("Недопустимое значение")

    def __add__(self, other):
        """
        Метод, реализуйющий возможность сложения экземпляров класса
        """
        if not isinstance(other, Item):
            raise ValueError("Складывать можно только объекты Item и дочерние от них.")
        return other.quantity + self.quantity
