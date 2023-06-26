import random
import time
from abc import ABC, abstractmethod

class Handler(ABC):
    """Component"""
    @abstractmethod
    def get(self):
        pass

class OrderController(Handler):
    """Concrete component"""
    def get(self):
        # sleep randomly 1-3s to "simulate" random access
        time.sleep(random.randrange(1, 3))
        return {"id":"123", "items": ["keyboard", "mouse"]}

class Decorator(Handler):
    def __init__(self, component):
        self.component = component

    def get(self):
        return self.component.get()

class LoggingDecorator(Decorator):
    def __init__(self, component):
        super().__init__(component)

    def get(self):
        print("Logging before request")
        response = self.component.get()
        print(f"Logging after request. Response {response}")
        return response

class TimingDecorator(Decorator):
    def __init__(self, component):
        super().__init__(component)

    def get(self):
        start = time.perf_counter()
        response = self.component.get()
        end = time.perf_counter()
        print(f"Time took for action {end - start}")
        return response

# **************************** Python decorators ****************************#
import functools

def logging(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Logging before request")
        response = func(*args, **kwargs)
        print(f"Logging after request. Response {response}")
        return response
    return wrapper

def timing(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        response = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Time took for action {end - start}")
        return response
    return wrapper

class ProfileController(Handler):
    @logging
    @timing
    def get(self):
        # sleep randomly 1-3s to "simulate" random access
        time.sleep(random.randrange(1, 3))
        return {"name": "John", "surname": "Doe", "account_id": 1234}