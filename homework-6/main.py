from src.item import Item
from src.settings import BROKEN_ITEMS_CSV_PATH

if __name__ == '__main__':
    # Файл items.csv отсутствует.
    Item.instantiate_from_csv("kkkkkk")
    # FileNotFoundError: Отсутствует файл item.csv

    # В файле items.csv удалена последняя колонка.
    Item.instantiate_from_csv(BROKEN_ITEMS_CSV_PATH)
    # InstantiateCSVError: Файл item.csv поврежден
