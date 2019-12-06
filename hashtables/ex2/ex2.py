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
    for item in tickets:
        hash_table_insert(hashtable, item.source, item.destination)
    route[0] = hash_table_retrieve(hashtable, "NONE")

    for i in range(1, length):
        result = hash_table_retrieve(hashtable, route[i-1])
        route[i] = result

    return route
