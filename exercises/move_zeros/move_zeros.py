def move_zeros(array):
    '''
    Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
    '''
    found = array.count(0)
    stringed = [str(i) for i in array]
    found_false = stringed.count("False")
    zeros = found - found_false
    filtered_list = list(filter(lambda a: a != 0 or type(a) == bool, array))
    to_be_appended = [0] * zeros
    filtered_list.extend(to_be_appended)
    return filtered_list
