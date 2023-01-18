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
        

fib = get_fibonacci(7)

for i in fib:
    pass