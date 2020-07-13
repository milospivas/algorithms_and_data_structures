''' Dynamic Programming: n-th Fibonacci number
'''

### Naive recursion

def fib_nr(n):
    ''' Returns n-th Fibonacci number.

    Naive recursive function.

    Parameters
    ----------
    n : int
        Index of the Fibonacci number to be returned.

    Returns
    -------
    int
        n-th Fibonacci number (starting from 1, 1,...)
    '''
    
    if n < 0:
        return None

    if n == 0:
        return 0

    elif n == 1:
        return 1

    else:
        return fib_nr(n-1) + fib_nr(n-2)



