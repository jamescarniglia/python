"""Find the continuous route"""


destinations = {'SEA': 'ORD', 'JFK': 'LAX', 'LAX': 'SEA', 'SFO': 'JFK' }

def find_routes(des):
    route = {}
    for key in des.keys():
        if key not in des.values():
            route[key] = des.get(key)
    while len(route) != len(des):
        route[list(route.values())[-1]] = des.get(list(route.values())[-1])
    return route



assert find_routes(destinations) == {'SFO': 'JFK', 'JFK': 'LAX', 'LAX': 'SEA', 'SEA': 'ORD'}
