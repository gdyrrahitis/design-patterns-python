# Define the state interface
class TicketPurchaseState:
    def select_movie(self, movie):
        pass

    def select_seats(self, seats):
        pass

    def process_payment(self):
        pass

    def cancel_purchase(self):
        pass

# Implement the concrete states
class IdleState(TicketPurchaseState):
    def __init__(self, context):
        self.ticket_purchase = context

    def select_movie(self, movie):
        print(f"Selected movie: {movie}.")
        # Transition to the SelectingSeatsState
        self.ticket_purchase.change_state(SelectingSeatsState(self.ticket_purchase))

    def select_seats(self, seats):
        print("Please select a movie first.")

    def process_payment(self):
        print("Please select a movie and seats before making a payment.")

    def cancel_purchase(self):
        print("No purchase to cancel.")

class SelectingSeatsState(TicketPurchaseState):
    def __init__(self, context):
        self.ticket_purchase = context

    def select_movie(self, movie):
        print("Movie already selected.")

    def select_seats(self, seats):
        print(f"Selected seats: {seats}.")
        # Transition to the PaymentProcessingState
        self.ticket_purchase.change_state(PaymentProcessingState(self.ticket_purchase))

    def process_payment(self):
        print("Please select seats before making a payment.")

    def cancel_purchase(self):
        print("Purchase cancelled.")
        # Transition back to the IdleState
        self.ticket_purchase.change_state(IdleState(self.ticket_purchase))

class PaymentProcessingState(TicketPurchaseState):
    def __init__(self, context):
        self.ticket_purchase = context

    def select_movie(self, movie):
        print("Movie already selected.")

    def select_seats(self, seats):
        print("Seats already selected.")

    def process_payment(self):
        print("Payment processed successfully.")
        # Transition to the CompletedPurchaseState
        self.ticket_purchase.change_state(CompletedPurchaseState())

    def cancel_purchase(self):
        print("Purchase cancelled.")
        # Transition back to the IdleState
        self.ticket_purchase.change_state(IdleState(self.ticket_purchase))

class CompletedPurchaseState(TicketPurchaseState):
    def select_movie(self, movie):
        print("Movie already selected.")

    def select_seats(self, seats):
        print("Seats already selected.")

    def process_payment(self):
        print("Payment already processed.")

    def cancel_purchase(self):
        print("Purchase already completed.")

# Define the ticket purchase class
class TicketPurchase:
    def __init__(self):
        # Initialize the ticket purchase with the IdleState
        self.state = IdleState(self)

    def select_movie(self, movie):
        self.state.select_movie(movie)

    def select_seats(self, seats):
        self.state.select_seats(seats)

    def process_payment(self):
        self.state.process_payment()

    def cancel_purchase(self):
        self.state.cancel_purchase()

    def change_state(self, state):
        self.state = state
