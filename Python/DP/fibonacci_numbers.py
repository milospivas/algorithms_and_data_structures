''' Dynamic Programming: n-th Fibonacci number

    Author: Milos Pivas, student
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


### testing

def test_fib(fib, ins = None, outs = None):
    ''' Test a function that calculates Fibonacci numbers.

    Parameters
    ----------
    fib : function handle
        The function to be tested

    Returns
    -------
    bool
        Passed/Not passed the test
    '''

    if ins is None:
        ins     = [   -1, 0, 1, 2, 3, 4, 5, 6, 7]
    if outs is None:
        outs    = [ None, 0, 1, 1, 2, 3, 5, 8, 13]

    for x, y in zip(ins, outs):
        if y != fib(x):
            return False
    
    return True



assert test_fib(fib_nr)

print('Exiting...')