import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate: float = 1.0
    all: list = []
    csv_file = "../src/items.csv"

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """

        self.__name: str = name
        self.price: float = price
        self.quantity: int = quantity
        Item.all.append(self)

    @property
    def name(self):
        """
        Геттер для name
        """
        return self.__name

    @name.setter
    def name(self, name):

        """
        Сеттер для name
        """
        if len(name) > 10:
            self.__name = name[:10]
        else:
            self.__name = name

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
        # cls.all.clear()
        # cls.all = []
        with open(csv_file, encoding='utf-8', errors='ignore') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['name']
                price = float(row["price"])
                amount = int(row['quantity'])
                cls(name, price, amount)

    @staticmethod
    def string_to_number(string):
        return int(len(string))
        # return int(string)

    # with open('names.csv', newline='') as csvfile:
    #     reader = csv.DictReader(csvfile)
    #     for row in reader:
    #         print(row['first_name'], row['last_name'])
