from abc import ABC, abstractmethod

class Request(ABC):
    def __init__(self, data = None):
        self.data = data

class RequestDirector:
    def __init__(self):
        self.handlers = {}

    def register(self, request, handler):
        self.handlers[request.__name__] = handler

    def send(self, request):
        handler = self.handlers[request.__class__.__name__]
        response = handler.handle(request)
        return response

class RequestHandler(ABC):
    @abstractmethod
    def handle(self):
        pass

class Ping(Request):
    pass

class Health(Request):
    pass

class PingHandler(RequestHandler):
    def __init__(self, mediator):
        self.mediator = mediator

    def handle(request):
        return "Pong"

class HealthHandler(RequestHandler):
    def __init__(self, mediator):
        self.mediator = mediator

    def handle(request):
        return "Healthy"