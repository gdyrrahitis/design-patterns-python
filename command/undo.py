from abc import ABC, abstractmethod

class Command(ABC):   
    @abstractmethod
    def execute(self, calculator):
        pass

    @abstractmethod
    def unexecute(self, calculator):
        pass


class Calculator:
    """Receiver"""
    def __init__(self):
        self.value = 0

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

class AddCommand(Command):
    """Concrete command"""
    def __init__(self, calculator, adder):
        self.adder = adder
        self.calculator = calculator
        self.previous_value = self.calculator.get_value()

    def execute(self):
        result = self.previous_value + self.adder
        self.calculator.set_value(result)

    def unexecute(self):
        self.calculator.set_value(self.previous_value)

class SubtractCommand(Command):
    """Concrete command"""
    def __init__(self, calculator, subtractor):
        self.subtractor = subtractor
        self.calculator = calculator
        self.previous_value = self.calculator.get_value()

    def execute(self):
        result = self.previous_value - self.subtractor
        self.calculator.set_value(result)

    def unexecute(self):
        self.calculator.set_value(self.previous_value)

class CalculationManager:
    """Invoker"""
    def __init__(self):
        self.stack = []

    def run_calculate_command(self, command):
        self.stack.append(command)
        command.execute()

    def rollback_calculcate_command(self):
        if self.stack:
            command = self.stack.pop()
            command.unexecute()

class CalculatorApplication:
    def __init__(self):
        self.calculationManager = CalculationManager()
        self.calculator = Calculator()
    
    def add(self, num):
        add_command = AddCommand(self.calculator, num)
        self.calculationManager.run_calculate_command(add_command)

    def subtract(self, num):
        subtract_command = SubtractCommand(self.calculator, num)
        self.calculationManager.run_calculate_command(subtract_command)
    
    def undo(self):
        self.calculationManager.rollback_calculcate_command()

    def get_current_value(self):
        return self.calculator.get_value()