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
    '''

    def __init__(self, cost, dx, dy):
        self.cost = cost
        self.dx = dx
        self.dy = dy


### Naive recursive DP

def edit_distance_nr(x, y, operations, i = 0, j = 0):
    ''' Calculate edit distance between strings x and y.

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
    int
        Computetd edit distance.
    '''

    if (i == len(x)) and (j == len(y)):
        return 0
    
    min_cost = float('Inf')
    # try available operations that surely transform the strings
    for o in operations:
        if (i + o.dx <= len(x)) and (j + o.dy <= len(y)):
            cost = o.cost + edit_distance_nr(x, y, operations, i + o.dx, j + o.dy)

            if cost < min_cost:
                min_cost = cost
    
    # try not doing anything if characters already match:
    if (i < len(x)) and (j < len(y)) and (x[i] == y[j]):
        cost = 0 + edit_distance_nr(x, y, operations, i+1, j+1)
        
        if cost < min_cost:
            min_cost = cost

    return min_cost


### Recursive DP + caching

def edit_distance_rc(x, y, operations, i = 0, j = 0, cache = None):
    ''' Calculate edit distance between strings x and y.

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
    int
        Computetd edit distance.
    '''

    if (i == len(x)) and (j == len(y)):
        return 0
    
    # cache init
    if cache is None:
        cache = {}

    min_cost = float('Inf')
    # try available operations that surely transform the strings
    for o in operations:
        if (i + o.dx <= len(x)) and (j + o.dy <= len(y)):
            next_i = i + o.dx
            next_j = j + o.dy

            if (next_i, next_j) in cache:
                next_cost = cache[(next_i, next_j)]
            else:
                next_cost = edit_distance_rc(x, y, operations, next_i, next_j, cache)

            cost = o.cost + next_cost

            if cost < min_cost:
                min_cost = cost
    
    # try not doing anything if characters already match:
    if (i < len(x)) and (j < len(y)) and (x[i] == y[j]):
        next_i, next_j = i+1, j+1
        
        if (next_i, next_j) in cache:
            cost = cache[(next_i, next_j)]
        else:
            cost = edit_distance_rc(x, y, operations, next_i, next_j, cache)

        if cost < min_cost:
            min_cost = cost

    # save in cache
    cache[(i, j)] = min_cost

    return min_cost


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
    int
        Computetd edit distance.
    '''

    for o in operations:
        if o.dx > 1 or o.dy > 1:
            raise Exception('Can\'t work with operations that use more than 1 character')
    
    # cache init
    cache = {}
    # start at the end of strings
    cache[(len(x), len(y))] = 0

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

                    next_cost = cache[(next_i, next_j)]
                    cost = o.cost + next_cost

                    if cost < min_cost:
                        min_cost = cost
                    
            # try not doing anything if characters already match:
            if (i < len(x)) and (j < len(y)) and (x[i] == y[j]):
                cost = cache[(i+1, j+1)]
                
                if cost < min_cost:
                    min_cost = cost

            # save in cache
            cache[(i, j)] = min_cost


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

    ed = edit_distance_func(x, y, operations)

    return ed == true_ed


help(edit_distance_nr)
help(edit_distance_rc)
help(edit_distance_bu)

# building operations list
delete = Operation(1, 1, 0)
insert = Operation(1, 0, 1)
replace = Operation(1, 1, 1)
operations = [delete, insert, replace]

x = 'a'
y = 'a'
true_ed = 0
assert test_ed(x, y, operations, true_ed, edit_distance_nr)
assert test_ed(x, y, operations, true_ed, edit_distance_rc)
assert test_ed(x, y, operations, true_ed, edit_distance_bu)

x = 'abacab'
y = 'ahab'
true_ed = 3
assert test_ed(x, y, operations, true_ed, edit_distance_nr)
assert test_ed(x, y, operations, true_ed, edit_distance_rc)
assert test_ed(x, y, operations, true_ed, edit_distance_bu)

print('Exiting...')