#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def recurse(ht, route, dest):
    route.append(dest)

    if dest != "NONE":
        recurse(ht, route, hash_table_retrieve(ht, dest))


def reconstruct_trip(tickets, length):
    ht = HashTable(length)
    route = []

    for ticket in tickets:
        hash_table_insert(ht, ticket.source, ticket.destination)

    recurse(ht, route, hash_table_retrieve(ht, "NONE"))

    return route
