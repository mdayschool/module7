
def get_list():
    inputs = []
    for i in range(0,3):
        inp = float(input("Input a number between 1 and 50: "))
        if inp >= 1 and inp <= 50:
            inputs.append(inp)
        else:
            raise ValueError("Input must be between 1 and 50")
    return inputs

def search_list(target):
    try:
        return get_list().index(target)
    except ValueError:
        return -1

def sort_list():
    ls = get_list()
    ls.sort()
    return ls

