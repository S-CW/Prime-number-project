import pytest
from inventory import *


def test_inventory_buy_sell():
    # Create inventory object
    inventory = Inventory()
    assert inventory.limit == 100
    assert inventory.total_items == 0

    # Add new Nike Sneaker
    inventory.add_new_stock("Nike Sneakers", 50.0, 10)
    assert inventory.total_items == 10

    # Add new Adidas Sweathpants
    inventory.add_new_stock("Adidas Sweatpants", 70.0, 5)
    assert inventory.total_items == 15

    # Remove items
    inventory.remove_stock("Nike Sneakers", 2)
    assert inventory.total_items == 13

    inventory.remove_stock("Adidas Sweatpants", 1)
    assert inventory.total_items == 12


def test_default_inventory():
    """Test default inventory limit is 100"""
    inventory = Inventory()
    assert inventory.limit == 100
    assert inventory.total_items == 0


def test_custom_inventory_limit():
    """Test that we can set a custom limit"""
    inventory = Inventory(limit=25)
    assert inventory.limit == 25
    assert inventory.total_items == 0


@pytest.fixture
def no_stock_inventory():
    """Returns an empty inventory that can store 10 items"""
    return Inventory(10)

# Multiple test case for quantity of 0, overlimit, and normal input
@pytest.mark.parametrize("name, price, quantity, exception", [("Test Jacket", 10.0, 0, InvalidQuantityException("Cannot add a quantity of 0. All stock must have atleast 1 item")), ("Test Jacket", 10.0, 25, NoSpaceException("Cannot add these 25 items. Only 10 items can be stored")), ("Test Jacket", 10.0, 5, None)])

def test_add_new_stock_limit(no_stock_inventory, name, price, quantity, exception):

    try:
        no_stock_inventory.add_new_stock(name, price, quantity)

    except (InvalidQuantityException, NoSpaceException) as inst:
        # Ensure exception is of the right type
        assert isinstance(inst, type(exception))
        # Ensure that the exceptions have the same message
        assert inst.args == exception.args

    # If no exception is raise and all goes accordingly
    else:
        assert no_stock_inventory.total_items == quantity
        assert no_stock_inventory.stocks[name]["price"] == price
        assert no_stock_inventory.stocks[name]["quantity"] == quantity

# Adds a fixture that contain some stock by default
@pytest.fixture
def stock_inventory():
    inventory = Inventory(20) # stock limit set to 20
    inventory.add_new_stock("Puma Test", 100.00, 8)
    inventory.add_new_stock("Reebok Test", 25.50, 2)
    return inventory


@pytest.mark.parametrize("name, quantity, exception, new_quantity, new_total", [("Puma Test", 0, ItemNotFoundException("Cannot remove items of 0. Must remove atleast 1 item"), 0, 0), ("Not Here", 5, ItemNotFoundException("Item Not Here does not exist. Cannot remove non-existing item in our stock"), 0, 0), ("Puma Test", 25, InvalidQuantityException("Cannot remove 25 items. Only 8 are in stock"), 0, 0), ("Puma Test", 5, None, 3, 5)])

def test_remove_stock(stock_inventory, name, quantity, exception, new_quantity, new_total):
    try:
        stock_inventory.remove_stock(name, quantity)
    except (ItemNotFoundException, InvalidQuantityException) as inst:
        
        assert isinstance(inst, type(exception))
        assert inst.args == exception.args
    else:
        assert stock_inventory.stocks[name]["quantity"] == new_quantity
        assert stock_inventory.total_items == new_total