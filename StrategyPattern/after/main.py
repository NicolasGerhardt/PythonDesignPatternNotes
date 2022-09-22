from abc import ABC, abstractmethod
import string
import random
from typing import List


def generate_id(length=8):
    # helper function for generating an id
    return ''.join(random.choices(string.ascii_uppercase, k=length))


class SupportTicket:

    def __init__(self, customer, issue):
        self.id = generate_id()
        self.customer = customer
        self.issue = issue


class TicketOrderingStrategy(ABC):
    @abstractmethod
    def create_ordering(self, ticket_list: List[SupportTicket]) -> List[SupportTicket]:
        pass


class FIFOOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, ticket_list: List[SupportTicket]) -> List[SupportTicket]:
        return ticket_list.copy()


class FILOOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, ticket_list: List[SupportTicket]) -> List[SupportTicket]:
        list_copy = ticket_list.copy()
        list_copy.reverse()
        return list_copy


class RandomOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, ticket_list: List[SupportTicket]) -> List[SupportTicket]:
        return random.shuffle(ticket_list.copy())


class BlackHoleOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, ticket_list: List[SupportTicket]) -> List[SupportTicket]:
        return []


class CustomerSupport:

    def __init__(self, processing_strategy: TicketOrderingStrategy):
        self.tickets = []
        self.processing_strategy = processing_strategy

    def create_ticket(self, customer, issue):
        self.tickets.append(SupportTicket(customer, issue))

    def process_tickets(self):
        ordered_list = self.processing_strategy.create_ordering(self.tickets)

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
app = CustomerSupport(BlackHoleOrderingStrategy())

# register a few tickets
app.create_ticket("John Smith", "My computer makes strange sounds!")
app.create_ticket("Linus Sebastian", "I can't upload any videos, please help.")
app.create_ticket("Arjan Egges", "VSCode doesn't automatically solve my bugs.")

# process the tickets
app.process_tickets()
