from abc import ABC, abstractmethod

class Command(ABC):   
    @abstractmethod
    def execute(self, calculator):
        pass

    @abstractmethod
    def unexecute(self, calculator):
        pass


class Calculator:
    def __init__(self):
        self.value = 0

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

class AddCommand(Command):
    def __init__(self, adder):
        self.adder = adder

    def execute(self, calculator):
        self.previous_value = calculator.get_value()
        result = self.previous_value + self.adder
        calculator.set_value(result)

    def unexecute(self, calculator):
        calculator.set_value(self.previous_value)

class SubtractCommand(Command):
    def __init__(self, subtractor):
        self.subtractor = subtractor

    def execute(self, calculator):
        self.previous_value = calculator.get_value()
        result = self.previous_value - self.subtractor
        calculator.set_value(result)

    def unexecute(self, calculator):
        calculator.set_value(self.previous_value)

class CalculatorApplication:
    def __init__(self, calculator):
        self.calculator = calculator
        self.stack = []

    def run_calculate_command(self, command):
        self.stack.append(command)
        command.execute(self.calculator)

    def rollback_calculcate_command(self):
        if self.stack:
            command = self.stack.pop()
            command.unexecute(self.calculator)

    def get_current_value(self):
        return self.calculator.get_value()
