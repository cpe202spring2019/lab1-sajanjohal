# some simple functions


def factorial(n): # assumes n non-negative integer, a number
    if (n == 0) :
        return 1
    else:
        return n * factorial(n-1)


def fib(n):
    """ Assumes n is non-negative integer"""
    if (n == 1) or (n == 0):
        return n
    else:
        return fib(n-1) + fib(n-2)


def maxlist_rec(tlist):
    if len(tlist) == 0:
        raise ValueError('empty list')
    elif len(tlist) == 1:
        return tlist[0]
    else:
        templist = tlist[1:len(tlist)]
        temp = maxlist_rec(templist)
        return max(tlist[0],temp)


def reverse_iter(temp_string):
    new_string = ""
    for i in range(len(temp_string)-1, -1, -1):
        new_string = new_string + temp_string[i]
    return new_string
