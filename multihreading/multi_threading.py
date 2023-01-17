# Example to elaborate multithreading in python

import threading


def cube(num):
    print("cube of {} is {}".format(num, num*num*num))


def square(num):
    print("square of {} is {}".format(num, num*num))


t1 = threading.Thread(target=cube, args=(10,))
t2 = threading.Thread(target=square, args=(10,))
t1.start()
t2.start()
t1.join()
t2.join()
print("Done!")
