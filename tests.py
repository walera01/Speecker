import time

def one(func):

    def wrap(*args, **kwargs):
        time1=time.time()
        print("++++++++++++++++++++++++++++++++")
        func(*args, **kwargs)
        time2 = time.time()
        print("--------------{}---------------".format(time1-time2))
        return True
    return wrap

@one
def second(a):
    for i in range(a):
        print(i)


print(second(100000))