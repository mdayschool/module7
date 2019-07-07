
def write_to_file(*args):
    try:
        with open('student_info.txt', 'a') as f:
            for arg in args:
                print("loop")
                f.write(str(arg) + " ")
            f.write('\n')
    except IOError as e:
        raise e

def get_student(name):
    scores = []
    while True:
        try:
            scores.append(int(input("Enter a test score "
                            + "or any other character to finish: ")))
        except ValueError:
            break
    return tuple([name] + scores)


def read_from_file():
    try:
        with open('student_info.txt', 'r') as f:
            lines = f.readlines()
            for line in lines:
                print(line)
    except IOError as e:
        raise e

if __name__=='__main__':
    try:
        """
        michael = get_student('Michael')
        write_to_file(*michael)
        erik = get_student('Erik')
        write_to_file(*erik)
        alex = get_student('Alex')
        write_to_file(*alex)
        adam = get_student('Adam')
        write_to_file(*adam)
        carl = get_student('Carl')
        write_to_file(*carl)
        """
        read_from_file()
    except Exception as e:
        print(str(e))
