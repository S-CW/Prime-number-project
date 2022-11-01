class InvalidQuantityException(Exception):
    pass

class NoSpaceException(Exception):
    pass

class ItemNotFoundException(Exception):
    pass


class Inventory:
    def __init__(self, limit=100) -> None:
        self.limit = limit
        self.total_items = 0
        self.stocks = {}

    def add_new_stock(self, name, price, quantity):
        

        if quantity <= 0:
            raise InvalidQuantityException("Cannot add a quantity of {}. All stock must have atleast 1 item".format(quantity))
            
        self.stocks[name] = {
        "price": price,
        "quantity": quantity
    }
        if quantity > self.limit:
            raise NoSpaceException("Cannot add these {} items. Only 10 items can be stored".format(quantity))

        self.total_items += quantity


    def remove_stock(self, name, quantity):
        if quantity <= 0:
            raise ItemNotFoundException("Cannot remove items of {}. Must remove atleast 1 item".format(quantity))
        if name not in self.stocks:
            raise ItemNotFoundException("Item {} does not exist. Cannot remove non-existing item in our stock".format(name))
        if quantity > self.stocks[name]["quantity"]:
            raise InvalidQuantityException("Cannot remove {} items. Only {} are in stock".format(quantity, self.stocks[name]["quantity"]))
        
        
        self.stocks[name]["quantity"] -= quantity
        self.total_items -= quantity



