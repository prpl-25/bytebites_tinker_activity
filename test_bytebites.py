from models import FoodItem, Menu, Transaction, Customer


def test_order_total():
    customer = Customer("Alice")
    order = Transaction(customer)
    order.add_item(FoodItem("Spicy Burger", 9.99, "Entrees", 4.5))
    order.add_item(FoodItem("Large Soda", 2.49, "Drinks", 3.8))
    assert round(order.compute_total(), 2) == 12.48


def test_empty_order_total():
    customer = Customer("Bob")
    order = Transaction(customer)
    assert order.compute_total() == 0.0


def test_filter_menu_by_category():
    menu = Menu()
    menu.add_item(FoodItem("Large Soda", 2.49, "Drinks", 3.8))
    menu.add_item(FoodItem("Lemonade", 3.00, "Drinks", 4.2))
    menu.add_item(FoodItem("Chocolate Cake", 5.00, "Desserts", 4.9))
    drinks = menu.filter_by_category("Drinks")
    assert len(drinks) == 2
    assert all(item.get_category() == "Drinks" for item in drinks)


def test_customer_is_verified_after_purchase():
    # Spec: purchase history verifies a customer is a real user
    customer = Customer("Alice")
    assert customer.is_verified() == False
    order = Transaction(customer)
    order.add_item(FoodItem("Spicy Burger", 9.99, "Entrees", 4.5))
    customer.add_transaction(order)
    assert customer.is_verified() == True


def test_filter_category_case_insensitive():
    menu = Menu()
    menu.add_item(FoodItem("Large Soda", 2.49, "Drinks", 3.8))
    assert len(menu.filter_by_category("drinks")) == 1
    assert len(menu.filter_by_category("DRINKS")) == 1
