#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    route_dict = {}

    for route in tickets:
        route_dict[route.source] = route.destination

    start_source = route_dict['NONE']
    places_list = [start_source]

    for i in range(length -1):
        next_source = places_list[i]
        next_destination = route_dict[next_source]
        places_list.append(next_destination)

    return places_list


