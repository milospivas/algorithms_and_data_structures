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

    ''' Loking at x[i] and y[j], for each i and j, options are:
            delete x[i],    costs 1
            insert y[j],    costs 1
            replace x[i] by y[j], costs 1
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


### testing
# building operations list
delete = Operation(1, 1, 0)
insert = Operation(1, 0, 1)
replace = Operation(1, 1, 1)
operations = [delete, insert, replace]

x = 'a'
y = 'a'
ed = edit_distance_nr(x, y, operations)
print('x:', x)
print('y:', y)
print('ed:', ed)

x = 'abacab'
y = 'ahab'
ed = edit_distance_nr(x, y, operations)
print('x:', x)
print('y:', y)
print('ed:', ed)

print('Exiting...')