from abc import ABC, abstractmethod

class Command(ABC):
    """The command interface"""
    def __init__(self, id):
        self.id = id
    
    @abstractmethod
    def execute(self):
        pass

class Repository:
    """Receiver"""
    def save(self, id, rating):
        print(f"Persisting rating of {rating} for product with id '{id}'")

    def update_stock(self, id, stock):
        print(f"Updating stock of product with id '{id}' to {stock}")

class UpdateStock(Command):
    """Concrete command"""
    def __init__(self, repository, id, stock):
        """Repository is receiver in this command"""
        super(UpdateStock, self).__init__(id=id)
        self.repository = repository
        self.stock = stock
    
    def execute(self):
        self.repository.update_stock(self.id, self.stock)

class RateProduct(Command):
    """Concrete command"""
    def __init__(self, repository, id, rating):
        """Repository is receiver in this command"""
        super(RateProduct, self).__init__(id=id)
        self.repository = repository
        self.rating = rating
    
    def execute(self):
        self.repository.save(self.id, self.rating)

class ProductHandler:
    """Invoker"""
    def handle(self, command):
        command.execute()
