from abc import ABC, abstractmethod

class PayrollTaxDirector:
    def __init__(self, tax):
        # tax is the strategy
        self.tax = tax

    def set_tax(self, tax):
        self.tax = tax

    """Context"""
    def calculate(self, price):
        return self.tax.calculate(price)

class Tax(ABC):
    """Strategy"""
    @abstractmethod
    def calculate(self, price):
        pass

class ProgressiveIncomeTax(Tax):
    def __init__(self):
        self.rate = 0.1

    """ConcreteStrategy1"""
    def calculate(self, salary):
        if salary <= 10000:
            return salary * 0.1
        elif salary <= 50000:
            return salary * 0.2
        else:
            return salary * 0.3

class NationalInsuranceTax(Tax):
    """ConcreteStrategy2"""
    def calculate(self, salary):
        if salary <= 30000:
            return salary * 0.1
        else:
            return salary * 0.15

class FlatRateIncomeTax(Tax):
    def __init__(self):
        self.rate = 0.25

    """ConcreteStrategy3"""
    def calculate(self, salary):
        return salary * self.rate
