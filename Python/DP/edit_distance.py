''' Dynamic Programming: Edit Distance
    "Given two strings x and y, what is the cheapest possible sequence of character edits
    (insert c, delete c, replace c -> c') to transform x into y?"

    It doesn't have to be strings and characters.
    The functions also work with any iterables whose elements can be compared with '==' operator.

    Author: Miloš Pivaš, student
'''


class Operation:
    ''' Describes an operation in computing edit distance, via its cost and which elements it uses.

    For more info on edit distance itself, see: https://en.wikipedia.org/wiki/Edit_distance

    Attributes
    ----------
    cost : int
        Operation cost
    dx : int
        The amount of elements in x the operation uses.
    dy : int
        The amount of elements in y the operation uses.

    Raises
    ------
    Exception
        Constructor raises 'Can\'t work with negative number of elements.'
        exception if negative values for dx or dy are passed to it.

    Examples
    --------
    delete = Operation(cost=1, dx=1, dy=0)
        # Represents deleting the current element in x, costs 1.

    insert = Operation(cost=1, dx=0, dy=1)
        # Represents inserting the current element from y into x, costs 1.

    replace = Operation(cost=1, dx=1, dy=1)
        # Represents replacing the current element in x with the current element in y, costs 1.
    '''

    def __init__(self, cost, dx, dy):
        ''' Constructor.

        See help(Operation) for more details.
        '''

        if dx < 0 or dy < 0:
            raise Exception('Can\'t work with negative number of elements.')
        self.cost = cost
        self.dx = dx
        self.dy = dy


### Naive recursive DP

def edit_distance_nr(x, y, operations):
    ''' Calculates edit distance between iterables x and y, using given operations.

    Naive recursive, dynamic programming method (without caching).

    Besides the given operations, doing nothing (if elements match) is always a possibility.

    For more info on edit distance itself, see: https://en.wikipedia.org/wiki/Edit_distance

    Parameters
    ----------
    x : iterable
        First input iterable. Must be sequential and elements must also support '==' operator.
    y : iterable
        Second input iterable. Must be sequential and elements must also support '==' operator.
    operations : list
        List of Operation() objects. List of available operations.

    Returns
    -------
    out : int, list
        int - Computed edit distance.
        list - of (operation, int, int) tuples describing what operation
        was performed on what element in x and y.
        operation is None if nothing was done.
        The first int is the index of the element in x.
        The second int is the index of the element in y.
    '''

    def __edit_distance(i = 0, j = 0):

        if (i == len(x)) and (j == len(y)):
            return 0, []

        min_cost = float('Inf')
        for operation in all_operations:
            curr_cost, next_i, next_j = operation.cost, i + operation.dx, j + operation.dy

            if (next_i <= len(x)) and (next_j <= len(y)):
                if (operation == do_nothing) and (x[i] != y[j]):
                    continue

                next_cost, next_operations = __edit_distance(next_i, next_j)
                cost = next_cost + curr_cost

                if cost < min_cost:
                    min_cost = cost
                    min_next_operations = next_operations + [(operation, i, j)]

        return min_cost, min_next_operations

    do_nothing = Operation(cost = 0, dx = 1, dy = 1)
    all_operations = operations + [do_nothing]
    sol = __edit_distance()
    return sol


### Recursive DP + caching

def edit_distance_rc(x, y, operations):
    ''' Calculates edit distance between iterables x and y.

    Recursive, dynamic programming method with caching (memoization).

    Besides the given operations, doing nothing (if elements match) is always a possibility.

    For more info on edit distance itself, see: https://en.wikipedia.org/wiki/Edit_distance

    Parameters
    ----------
    x : iterable
        First input iterable. Must be sequential and elements must also support '==' operator.
    y : iterable
        Second input iterable. Must be sequential and elements must also support '==' operator.
    operations : list
        List of Operation() objects. List of available operations.

    Returns
    -------
    out : int, list
        int - Computed edit distance.
        list - of (operation, int, int) tuples describing what operation
        was performed on what element in x and y.
        operation is None if nothing was done.
        The first int is the index of the element in x.
        The second int is the index of the element in y.
    '''

    def __cache_init():
        cache = {}
        cache[len(x), len(y)] = 0, []
        return cache

    def __edit_distance_with_caching(i = 0, j = 0):

        if (i, j) in cache:
            return cache[i, j]

        min_cost = float('Inf')
        for operation in all_operations:
            curr_cost, next_i, next_j = operation.cost, i + operation.dx, j + operation.dy

            if (next_i <= len(x)) and (next_j <= len(y)):
                if (operation == do_nothing) and (x[i] != y[j]):
                    continue

                next_cost, next_operations = __edit_distance_with_caching(next_i, next_j)
                cost = next_cost + curr_cost

                if cost < min_cost:
                    min_cost = cost
                    min_next_operations = next_operations + [(operation, i, j)]

        cache[i, j] = min_cost, min_next_operations

        return min_cost, min_next_operations

    cache = __cache_init()
    do_nothing = Operation(cost = 0, dx = 1, dy = 1)
    all_operations = operations + [do_nothing]
    sol = __edit_distance_with_caching()
    return sol


### Iterative, bottom-up DP with caching

def edit_distance_bu(x, y, operations):
    ''' Calculates edit distance between iterables x and y.

    Iterative, bottom-up, dynamic programming method.

    Besides the given operations, doing nothing (if elements match) is always a possibility.

    For more info on edit distance itself, see: https://en.wikipedia.org/wiki/Edit_distance

    Parameters
    ----------
    x : iterable
        First input iterable. Must be sequential and elements must also support '==' operator.
    y : iterable
        Second input iterable. Must be sequential and elements must also support '==' operator.
    operations : list
        List of Operation() objects. List of available operations.

    Returns
    -------
    out : int, list
        int - Computed edit distance.
        list - of (operation, int, int) tuples describing what operation
        was performed on what element in x and y.
        operation is None if nothing was done.
        The first int is the index of the element in x.
        The second int is the index of the element in y.

    Raises
    ------
    Exception
        'Can\'t work with operations that use more than 1 element'
        if any given operation uses more than 1 element per iterable.
    '''

    def __cache_init():
        cache = {}
        cache[len(x), len(y)] = 0, []
        return cache

    def __get_topological_order():
        ''' We look at the cache as a len(x)+1 by len(y)+1 matrix M[i][j].
            We start in the lower right corner, cache[(len(x), len(y))],
            after the ends of x and y. That's our base case.
            Then we will move to the first field - one "left".
            And then we will move "up-right", on each line parallel to the antidiagonal,
            like so:\n
            _________/9\n
            _______/8/5\n
            _____/7/4/2\n
            ___/6/3/1/0\n
        '''

        # the first field after the base case:
        i_line_start, j_line_start = len(x), len(y)-1
        on_the_grid = True
        while on_the_grid:

            i, j = i_line_start, j_line_start
            on_the_line = True
            while on_the_line:

                yield i, j

                # move to the next element in the line ("up-right")
                i -= 1
                j += 1

                if i < 0 or j > len(y):
                    on_the_line = False

            # move to the next line:
            if j_line_start-1 >= 0:     # until the start of the lower edge,
                j_line_start -= 1       #   move "left"
            elif i_line_start-1 >= 0:   # else, until the start of the left edge
                i_line_start -= 1       #   move "up"
            else:                       # else:
                on_the_grid = False     #   we're done


    for operation in operations:
        if operation.dx > 1 or operation.dy > 1:
            raise Exception('Can\'t work with operations that use more than 1 element')

    cache = __cache_init()
    do_nothing = Operation(cost = 0, dx = 1, dy = 1)
    all_operations = operations + [do_nothing]

    topological_order = __get_topological_order()

    for i, j in topological_order:
        min_cost = float('Inf')
        for operation in all_operations:
            curr_cost, next_i, next_j = operation.cost, i + operation.dx, j + operation.dy

            if (next_i <= len(x)) and (next_j <= len(y)):
                if (operation == do_nothing) and (x[i] != y[j]):
                    continue

                next_cost, next_operations = cache[next_i, next_j]
                cost = next_cost + curr_cost

                if cost < min_cost:
                    min_cost = cost
                    min_next_operations = next_operations + [(operation, i, j)]

        cache[i, j] = min_cost, min_next_operations

        # this optimises the cache space to use only O(len(x)+len(y)) space, instead of O(len(x)*len(y)),
        # by removing the no longer needed elements from the second-previous line bellow
        cache.pop((i+2, j), None)

    return cache[0,0]


### testing

def test_ed(x, y, operations, true_ed, edit_distance_func):
    ''' Auto tests edit distance function

    Parameters
    ----------
    x : iterable
        First input iterable. Must be sequential and elements must also support '==' operator.
    y : iterable
        Second input iterable. Must be sequential and elements must also support '==' operator.
    operations : list
        List of Operation() objects. List of available operations.
    true_ed : int
        True solution
    edit_distance_func : function handle
        Function to be tested with following interface:
            Parameters
            ----------
            x : iterable
                First input iterable. Must be sequential and elements must also support '==' operator.
            y : iterable
                Second input iterable. Must be sequential and elements must also support '==' operator.
            operations : list
                List of Operation() objects. List of available operations.

            Returns
            -------
            out : int, list
                int - Computed edit distance.
                list - of (operation, int, int) tuples describing what operation
                was performed on what element in x and y.
                operation is None if nothing was done.
                The first int is the index of the element in x.
                The second int is the index of the element in y.

    Returns
    -------
    out : bool
        Passed/Not passed the test.
    '''

    ed, _ = edit_distance_func(x, y, operations)

    return ed == true_ed


help(Operation)

# Can't work with negative number of elements
try:
    o = Operation(42, -1, 0)
except Exception as e:
    print(e)

try:
    o = Operation(42, 0, -1)
except Exception as e:
    print(e)

help(edit_distance_nr)
help(edit_distance_rc)
help(edit_distance_bu)

# building operations list (for calculating, the Levenshtein distance)
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

x = [1,2,1,3,1,2]   # represents 'abacab'
y = [1,8,1,2]       # represents 'ahab'
true_ed = 3
assert test_ed(x, y, operations, true_ed, edit_distance_nr)
assert test_ed(x, y, operations, true_ed, edit_distance_rc)
assert test_ed(x, y, operations, true_ed, edit_distance_bu)

import numpy as np
x_arr = np.array(x)
y_arr = np.array(y)
assert test_ed(x_arr, y_arr, operations, true_ed, edit_distance_nr)
assert test_ed(x_arr, y_arr, operations, true_ed, edit_distance_rc)
assert test_ed(x_arr, y_arr, operations, true_ed, edit_distance_bu)

print('Exiting...')