''' Dynamic Programming: Edit Distance
    "Given two strings x and y, what is the cheapest possible sequence of character edits
    (insert c, delete c, replace c -> c') to transform x into y?"

    Author: Miloš Pivaš, student
'''


class Operation:
    ''' Describes an operation via its cost and which characters it uses.
    
    Attributes
    ----------
    cost : int
        Operation cost
    dx : int
        The amount of characters in x the operation uses.
    dy : int
        The amount of characters in y the operation uses.

    Raises
    ------
    Exception
        Constructor raises 'Can\'t work with negative number of characters.'
        exception if negative values for dx or dy are passed to it.
        
    '''

    def __init__(self, cost, dx, dy):
        ''' Constructor.

        See help(Operation) for more details.
        '''

        if dx < 0 or dy < 0:
            raise Exception('Can\'t work with negative number of characters.')
        self.cost = cost
        self.dx = dx
        self.dy = dy


### Naive recursive DP

def edit_distance_nr(x, y, operations, i = 0, j = 0):
    ''' Calculates edit distance between strings x and y.

    Naive recursive, dynamic programming method (without caching).

    Parameters
    ----------
    x : str
        First string.
    y : str
        Second string.
    operations : list
        List of available operations
    [i : int]
        Starting index of the first string.
    [j : int]
        Starting index of the second string.

    Returns
    -------
    int, list
        int - Computed edit distance.
        list - of (operation, int, int) tuples describing what operation
        was performed on what characters in x and y.
        operation is None if nothing was done.
        The first int is the index of the character in x.
        The second int is the index of the character in y.
    '''

    if (i == len(x)) and (j == len(y)):
        return 0, []
    
    min_cost = float('Inf')
    # try available operations that surely transform the strings
    for o in operations:
        next_i, next_j = i + o.dx, j + o.dy
        
        if (next_i <= len(x)) and (next_j <= len(y)):
            next_cost, next_operations = edit_distance_nr(x, y, operations, next_i, next_j)
            cost = next_cost + o.cost 

            if cost < min_cost:
                min_cost = cost
                min_next_operations = next_operations + [(o, i, j)]
    
    # try not doing anything if characters already match:
    if (i < len(x)) and (j < len(y)) and (x[i] == y[j]):
        cost, next_operations = edit_distance_nr(x, y, operations, i+1, j+1)
        
        if cost < min_cost:
            min_cost = cost
            min_next_operations = next_operations + [(None, i, j)]
        
    return min_cost, min_next_operations


### Recursive DP + caching

def edit_distance_rc(x, y, operations, i = 0, j = 0, cache = None):
    ''' Calculates edit distance between strings x and y.

    Recursive, dynamic programming method with caching (memoization).

    Parameters
    ----------
    x : str
        First string.
    y : str
        Second string.
    operations : list
        List of available operations
    [i : int]
        Starting index of the first string.
    [j : int]
        Starting index of the second string.
    [cache : dict]
        Hashmap of already computed solutions.

    Returns
    -------
    int, list
        int - Computed edit distance.
        list - of (operation, int, int) tuples describing what operation
        was performed on what characters in x and y.
        operation is None if nothing was done.
        The first int is the index of the character in x.
        The second int is the index of the character in y.
    '''

    if (i == len(x)) and (j == len(y)):
        return 0, []
    
    # cache init
    if cache is None:
        cache = {}

    min_cost = float('Inf')
    # try available operations that surely transform the strings
    for o in operations:
        if (i + o.dx <= len(x)) and (j + o.dy <= len(y)):
            next_i, next_j = i + o.dx, j + o.dy

            if (next_i, next_j) in cache:
                next_cost, next_operations = cache[(next_i, next_j)]
            else:
                next_cost, next_operations = edit_distance_rc(x, y, operations, next_i, next_j, cache)

            cost = o.cost + next_cost

            if cost < min_cost:
                min_cost = cost
                min_next_operations = next_operations + [(o, i, j)]
    
    # try not doing anything if characters already match:
    if (i < len(x)) and (j < len(y)) and (x[i] == y[j]):
        next_i, next_j = i+1, j+1
        
        if (next_i, next_j) in cache:
            cost, next_operations = cache[(next_i, next_j)]
        else:
            cost, next_operations = edit_distance_rc(x, y, operations, next_i, next_j, cache)

        if cost < min_cost:
            min_cost = cost
            min_next_operations = next_operations + [(None, i, j)]

    # save in cache
    cache[(i, j)] = min_cost, min_next_operations

    return min_cost, min_next_operations


### Iterative, bottom-up DP with caching

def edit_distance_bu(x, y, operations):
    ''' Calculates edit distance between strings x and y.
    
    Iterative, bottom-up, dynamic programming method.

    Parameters
    ----------
    x : str
        First string.
    y : str
        Second string.
    operations : list
        List of available operations

    Returns
    -------
    int, list
        int - Computed edit distance.
        list - of (operation, int, int) tuples describing what operation
        was performed on what characters in x and y.
        operation is None if nothing was done.
        The first int is the index of the character in x.
        The second int is the index of the character in y.

    Raises
    ------
    Exception
        'Can\'t work with operations that use more than 1 character'
        if any given operation uses more than 1 character per string.
    '''

    for o in operations:
        if o.dx > 1 or o.dy > 1:
            raise Exception('Can\'t work with operations that use more than 1 character')
    
    # cache init
    cache = {}
    # start at the end of strings
    cache[(len(x), len(y))] = 0, []

    # move "left"
    i_start, j_start = len(x), len(y)-1

    while True:
        # get the starting point
        i, j = i_start, j_start

        while True:
            # process the element

            min_cost = float('Inf')
            # try available operations that surely transform the strings
            for o in operations:
                if (i + o.dx <= len(x)) and (j + o.dy <= len(y)):
                    next_i, next_j = i + o.dx, j + o.dy

                    next_cost, next_operations = cache[(next_i, next_j)]
                    cost = o.cost + next_cost

                    if cost < min_cost:
                        min_cost = cost
                        min_next_operations = next_operations + [(o, i, j)]

                    
            # try not doing anything if characters already match:
            if (i < len(x)) and (j < len(y)) and (x[i] == y[j]):
                cost, next_operations = cache[(i+1, j+1)]
                
                if cost < min_cost:
                    min_cost = cost
                    min_next_operations = next_operations + [(None, i, j)]

            # save in cache
            cache[(i, j)] = min_cost, min_next_operations

            # this optimises the cache space to use only O(len(x)+len(y)) space
            # instead of O(len(x)*len(y))
            if (i+2, j) in cache:
                cache.pop(i+2, j)
            if (i, j+2) in cache:
                cache.pop(i, j+2)

            # move to the next element
            i -= 1
            j += 1
            # if off the grid, move to the next starting point
            if i < 0 or j > len(y):
                break
        
        if j_start-1 >= 0:      # if possible
            j_start -= 1        #   move "left"
        elif i_start-1 >= 0:    # else, if possible
            i_start -= 1        #   move "up"
        else:                   # else:
            break               #   we're done

    return cache[(0,0)]


### testing

def test_ed(x, y, operations, true_ed, edit_distance_func):
    ''' Auto tests edit distance function

    Parameters
    ----------
    x : str
        First string.
    y : str
        Second string.
    operations : list
        List of available operations
    true_ed : int
        True solution
    edit_distance_func : function handle
        Function to be tested with following interface:
            Parameters
            ----------
            x : str
                First string.
            y : str
                Second string.
            operations : list
                List of available operations

            Returns
            -------
            int
                Computetd edit distance.

    Returns
    -------
    bool
        Passed/Not passed the test.
    '''

    ed, _ = edit_distance_func(x, y, operations)

    return ed == true_ed


# help(Operation)

# # Can't work with negative number of characters
# try:
#     o = Operation(42, -1, 0)
# except Exception as e:
#     print(e)

# try:
#     o = Operation(42, 0, -1)
# except Exception as e:
#     print(e)

# help(edit_distance_nr)
# help(edit_distance_rc)
# help(edit_distance_bu)

# # building operations list
# delete = Operation(1, 1, 0)
# insert = Operation(1, 0, 1)
# replace = Operation(1, 1, 1)
# operations = [delete, insert, replace]

# x = 'a'
# y = 'a'
# true_ed = 0
# assert test_ed(x, y, operations, true_ed, edit_distance_nr)
# assert test_ed(x, y, operations, true_ed, edit_distance_rc)
# assert test_ed(x, y, operations, true_ed, edit_distance_bu)

# x = 'abacab'
# y = 'ahab'
# true_ed = 3
# assert test_ed(x, y, operations, true_ed, edit_distance_nr)
# assert test_ed(x, y, operations, true_ed, edit_distance_rc)
# assert test_ed(x, y, operations, true_ed, edit_distance_bu)

# print('Exiting...')