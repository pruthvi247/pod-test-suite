import time

def measuretime(func):
    def wrapper():
        print("Dont waste time")
        starttime = time.perf_counter()
        func()
        endtime = time.perf_counter()
        print(f"Time needed: {endtime - starttime} seconds")
    return wrapper
@measuretime
def wastetime():
    print("Time waste")
    sum([i**2 for i in range(1000000)])
wastetime()


# i = 0
str = 'fghjkldjklrtyuiopcvbnm,.'
for i,letter in enumerate(str):
    print("The letter at index %i is %s" % (i, letter))
    # i = i + 1