class FoodItem:
    def __init__(self, name: str, price: float, category: str, popularity_rating: float):
        if price < 0:
            raise ValueError("Price cannot be negative")
        if not (0.0 <= popularity_rating <= 5.0):
            raise ValueError("Popularity rating must be between 0.0 and 5.0")
        self.__name = name
        self.__price = price
        self.__category = category
        self.__popularity_rating = popularity_rating

    def get_name(self) -> str:
        return self.__name

    def get_price(self) -> float:
        return self.__price

    def get_category(self) -> str:
        return self.__category

    def get_popularity_rating(self) -> float:
        return self.__popularity_rating

    def __str__(self) -> str:
        return f"{self.__name} (${self.__price:.2f}) [{self.__category}] ★{self.__popularity_rating}"


class Menu:
    def __init__(self):
        self.__items = []

    def add_item(self, item: FoodItem) -> None:
        self.__items.append(item)

    def remove_item(self, item: FoodItem) -> None:
        if item in self.__items:
            self.__items.remove(item)

    def filter_by_category(self, category: str) -> list:
        return [item for item in self.__items if item.get_category().lower() == category.lower()]

    def get_all_items(self) -> list:
        return list(self.__items)


class Transaction:
    def __init__(self, customer):
        self.__customer = customer
        self.__selected_items = []

    def add_item(self, item: FoodItem) -> None:
        if item is None:
            raise ValueError("Cannot add a null item to a transaction")
        self.__selected_items.append(item)

    def compute_total(self) -> float:
        return sum(item.get_price() for item in self.__selected_items)

    def get_selected_items(self) -> list:
        return list(self.__selected_items)

    def get_customer(self) -> "Customer":
        return self.__customer


class Customer:
    def __init__(self, name: str):
        if not name or not name.strip():
            raise ValueError("Customer name cannot be empty")
        self.__name = name
        self.__purchase_history = []

    def get_name(self) -> str:
        return self.__name

    def get_purchase_history(self) -> list:
        return list(self.__purchase_history)

    def add_transaction(self, transaction: Transaction) -> None:
        self.__purchase_history.append(transaction)

    def is_verified(self) -> bool:
        return len(self.__purchase_history) > 0