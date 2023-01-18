def get_fibonacci(num):
    a,b = 0,1
    indx = 0
    if indx == 0:
        print(a)
    while indx <= num-2:
        print(b)
        indx += 1
        yield 
        b,a = a+b, b
        



## Example of decorator


def decorate(func):
    def closure(a,b):
        print("decorating Before calling main func")
        func(a, b)
        print("decorating after main function")
    return closure

@decorate
def sum_numbers(a, b):
    print("sum of {0} and {1} is: {2}".format(a,b,a+b))


if __name__ == "__main__":
    fib = get_fibonacci(7)

    for i in fib:
        pass

    sum_numbers(4,5)