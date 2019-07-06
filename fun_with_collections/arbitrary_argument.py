
def average_scores(*args, **kwargs):
    total = 0
    count = 0
    ave = 0
    for arg in args:
        total += arg
        count += 1
    if ave > 0:
        ave = total / args.length
    kvs = ""
    for k,v in kwargs.items():
        kvs += " k:" + k + " v:" + v
    return "Average: " + str(ave) + " Pairs: " + kvs

if __name__=='__main__':
    print(average_scores(4,5,6,7,first_name='Michael', last_name='Day',
                         major='Subversion_of_Authority'))
