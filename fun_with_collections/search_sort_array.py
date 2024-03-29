import array

def get_list():
    """Gets and validates 3 inputs"""
    inputs = []
    for i in range(0,3):
        inp = float(input("Input a number between 1 and 50: "))
        if inp >= 1 and inp <= 50:
            inputs.append(inp)
        else:
            raise ValueError("Input must be between 1 and 50")
    return inputs

def search_list(target):
    """Searches list and returns -1 for value error"""
    try:
        return get_list().index(target)
    except ValueError:
        return -1

def sort_list():
    """
    Sorts list - Returns a list because otherwise
    it would just be generating garbage
    """
    ls = get_list()
    ls.sort()
    return ls

def sort_array():
    """
    Sorts array - Returns an array becase otherwise
    it would just be generating garbage.
    """
    ls = get_list()
    ls.sort()
    arr = array.array('f', ls)
    return arr
