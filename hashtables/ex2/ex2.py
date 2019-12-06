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


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    print('  h:   ',tickets[0].destination)
    for item in tickets:
        hash_table_insert(hashtable, item.source, item.destination)

    for i in range(length):
        result = hash_table_retrieve(hashtable, item.source)
        route[i] = result

    return route
