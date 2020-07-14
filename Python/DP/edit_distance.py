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


# building operations list
delete = Operation(1, 1, 0)
insert = Operation(1, 0, 1)
replace = Operation(1, 1, 1)
operations = [delete, insert, replace]