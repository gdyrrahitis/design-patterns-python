from abc import ABC, abstractmethod
from time import sleep

class Subject(ABC):
    def __init__(self):
        self.observers = {}

    def __del__(self):
        # unsubscribing observers when object is destroyed
        print("Calling destructor")
        observers = self.observers.copy().values()
        for observer in observers:
            self.detach(observer)

    def attach(self, observer):
        observer_name = observer.__class__.__name__
        print(f"Adding observer {observer_name} to subject {self.__class__.__name__}")
        self.observers[observer_name] = observer

    def detach(self, observer):
        removed = self.observers.pop(observer.__class__.__name__)
        print(f"Removed observer {removed.__class__.__name__} from subject {self.__class__.__name__}")

    def notify(self):
        for observer in self.observers.values():
            observer.update(self)

class Observer(ABC):
    @abstractmethod
    def update(self, subject):
        pass

class RPiNodesUpdaterWorkflow(Subject):
    def __init__(self):
        super().__init__()
        self.steps = [
            {
                "name": "retrieve_state_of_nodes",
                "status": "not_started"
            },
            {
                "name": "check_if_node_needs_update",
                "status": "not_started"
            },
            {
                "name": "update_nodes",
                "status": "not_started"
            },
            {
                "name": "reboot_nodes",
                "status": "not_started"
            }
        ]
        self.status = "not_started"
        self.current_step = None
        self.workflow_name = self.__class__.__name__

    def start(self):
        print("Workflow started")
        self.current_step = self.steps[0]
        self.status = "running"
        self.notify()

    def _get_current_step_name(self):
        return self.current_step["name"]

    def run_step(self):
        current_step_name = self._get_current_step_name()
        print(f"Running {current_step_name}...")
        sleep(1)
        self.current_step["status"] = "completed"
        print(f"Completed! Successful execution of {current_step_name}")
        self.notify()

        next = self.steps.index(self.current_step) + 1
        if next > len(self.steps) - 1:
            self._workflow_completed()
            return

        self.current_step = self.steps[next]
        current_step_name = self._get_current_step_name()
        print(f"Next step to run: {current_step_name}")

    def _workflow_completed(self):
        print(f"Workflow completed all its steps!")
        self.status = "completed"
        self.current_step = None
        self.notify()

    def get_workflow_status(self):
        return {
            "workflow_name": self.workflow_name,
            "workflow_status": self.status,
            "current_step": self.current_step
        }


class SlackNotificationHandler(Observer):
    def __init__(self):
        self.channel = "#my_awesome_team_channel"

    def update(self, subject):
        self.subject = subject
        self.notify_on_workflow_state()

    def notify_on_workflow_state(self):
        workflow = self.subject.get_workflow_status()
        workflow_name = workflow["workflow_name"]
        print("\n\n***** Slack Notification *****\n")
        print(f"Sending DM to slack channel {self.channel} on workflow {workflow_name}\n{workflow}\n")

class EmailNotificationHandler(Observer):
    def __init__(self):
        self.email = "my_awesome_company@company.com"

    def update(self, subject):
        self.subject = subject
        self.notify_on_workflow_state()

    def notify_on_workflow_state(self):
        workflow = self.subject.get_workflow_status()
        workflow_name = workflow["workflow_name"]
        print("\n\n***** Email Notification *****\n")
        print(f"Sending email to {self.email} on workflow {workflow_name}\n{workflow}\n")