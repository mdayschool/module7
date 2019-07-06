
def get_list():
    print("testtesttest")
    inputs = []
    for i in range(0,3):
        inp = float(input("Input a number between 1 and 50: "))
        if inp >= 1:
            inputs.append(inp)
        else:
            raise ValueError("Input must be between 1 and 50")
    return inputs
