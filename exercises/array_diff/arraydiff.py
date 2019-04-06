def array_diff(a, b):
    """
    implement a difference function, which subtracts
    one list from another and returns the result.
    """
    return list(filter(lambda x: x not in b, a))
