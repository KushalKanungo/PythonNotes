# a small anonymous function can have multiple arguments but can have only one expression

def x(a, b, c): return a+b+c


print(x(5, 3, 6))
print(x(78, 56, 55))

# The power of lambda is better shown when you use them as an anonymous function inside another function.


def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)
# above simplified mydouble=lamda a:a*2
print(mydoubler(11))

