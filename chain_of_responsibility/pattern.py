from abc import ABC, abstractmethod

class Incident:
    """Request"""
    def __init__(self, type, info):
        self.type = type
        self.info = info

class ClinicalDepartment(ABC):
    """Handler"""
    def __init__(self):
        self.adjacent = None

    @abstractmethod
    def handle(self, incident):
        pass

    def set_adjacent(self, adjacent):
        self.adjacent = adjacent
    
    def adjacent_handle_or_default(self, incident):
        if self.adjacent:
            self.adjacent.handle(incident)
        else:
            print("Cannot handle incident - refer to other hospital")

class Emergency(ClinicalDepartment):
    """ConcreteHandler"""
    def handle(self, incident):
        if incident.type == "emergency":
            print(incident.info)
            print("Handling emergency incident - notifying E&A doctor")
        else:
            self.adjacent_handle_or_default(incident)

class Labs(ClinicalDepartment):
    """ConcreteHandler"""
    def handle(self, incident):
        if incident.type == "labs":
            print(incident.info)
            print("Handling lab specimen - notifying laboratory personnel")
        else:
            self.adjacent_handle_or_default(incident)

class Surgery(ClinicalDepartment):
    """ConcreteHandler"""
    def handle(self, incident):
        if incident.type == "surgery":
            print(incident.info)
            print("Handling surgery - notifying surgeon")
        else:
            self.adjacent_handle_or_default(incident)

class Hospital:
    """Client"""
    def set_department_graph(self, department):
        self.department = department

    def handle(self, incident):
        self.department.handle(incident)