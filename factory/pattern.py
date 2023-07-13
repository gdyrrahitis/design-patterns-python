from abc import ABC, abstractmethod

class Order(ABC):
    """Product"""
    def __init__(self, id, customer, items):
        self.id = id
        self.customer = customer
        self.items = items
        self.status = "created"

    def add_item(self, item):
        self.items.append(item)
    
    def remove_item(self, item):
        self.items.remove(item)
    
    @abstractmethod
    def process_order(self):
        pass

    @abstractmethod
    def cancel_order(self):
        pass

class StandardOrder(Order):
    """ConcreteProduct"""
    def process_order(self):
        if self.status == "created":
            self.status = "processed"
            print("Updating inventory...")
            print(f"Notifying customer {self.customer}...")
        else:
            raise Exception("Invalid order status for processing the order")

    def cancel_order(self):
        if self.status == "processed":
            self.status = "cancelled"
            print("Restocking inventory...")
            print(f"Refunding customer {self.customer}...")
        else:
            raise Exception("Invalid order status for cancelling the order")

class PreOrder(Order):
    """ConcreteProduct"""
    def process_order(self):
        if self.status == "created":
            self.status = "preordered"
            print(f"Notifying customer {self.customer} about release date...")
        else:
            raise Exception("Invalid order status for processing the pre-order")

    def cancel_order(self):
        if self.status == "preordered":
            self.status = "cancelled"
            print(f"Notifying customer {self.customer} about cancellation...")
        else:
            raise Exception("Invalid order status for cancelling the pre-order")

class OrderCreator(ABC):
    """Creator"""
    @abstractmethod
    def create_order(self, id, customer, items):
        pass

class StandardOrderCreator(OrderCreator):
    """ConcreteCreator"""
    def create_order(self, id, customer, items):
        return StandardOrder(id, customer, items)

class PreOrderCreator(OrderCreator):
    """ConcreteCreator"""
    def create_order(self, id, customer, items):
        return PreOrder(id, customer, items)
