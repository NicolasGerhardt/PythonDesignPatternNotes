import string
import random
from typing import Callable, List


def generate_id(length=8):
    # helper function for generating an id
    return ''.join(random.choices(string.ascii_uppercase, k=length))


class SupportTicket:

    def __init__(self, customer, issue):
        self.id = generate_id()
        self.customer = customer
        self.issue = issue


def fifo_ordering(ticket_list: List[SupportTicket]) -> List[SupportTicket]:
    return ticket_list.copy()


def filo_ordering(ticket_list: List[SupportTicket]) -> List[SupportTicket]:
    list_copy = ticket_list.copy()
    list_copy.reverse()
    return list_copy


def random_ordering(ticket_list: List[SupportTicket]) -> List[SupportTicket]:
    return random.shuffle(ticket_list.copy())


def black_hole_ordering(ticket_list: List[SupportTicket]) -> List[SupportTicket]:
    return []


class CustomerSupport:

    def __init__(self, processing_strategy_fn: Callable[[List[SupportTicket]], List[SupportTicket]]):
        self.tickets = []
        self.processing_strategy_fn = processing_strategy_fn

    def create_ticket(self, customer, issue):
        self.tickets.append(SupportTicket(customer, issue))

    def process_tickets(self):
        ordered_list = self.processing_strategy_fn(self.tickets)

        # if it's empty, don't do anything
        if len(ordered_list) == 0:
            print("There are no tickets to process. Well done!")
            return

        for ticket in ordered_list:
            self.process_ticket(ticket)

    def process_ticket(self, ticket: SupportTicket):
        print("==================================")
        print(f"Processing ticket id: {ticket.id}")
        print(f"Customer: {ticket.customer}")
        print(f"Issue: {ticket.issue}")
        print("==================================")


# create the application
app = CustomerSupport(filo_ordering)

# register a few tickets
app.create_ticket("John Smith", "My computer makes strange sounds!")
app.create_ticket("Arjan Egges", "Co-pilot will never put me out of business")
app.create_ticket("Nic Heart", "All I want for x-mas is a soundbar")

# process the tickets
app.process_tickets()
