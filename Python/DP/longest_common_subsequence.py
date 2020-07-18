''' Dynamic Programming: Longest Common Subsequence

    Depends on: edit_distance.py

    Works with iterables of any type, but, of course,
    in realistic use cases, this would be implemented as a class method,
    dedicated to specific type.

    Author: Miloš Pivaš
'''

from edit_distance import Operation
from edit_distance import edit_distance_bu


def longest_common_subsequence(x, y, empty_object = None, append_func = None):
    ''' Finds the longest common subsequence in two given iterables.

    Subsequence is sequential but doesn't have to be contiguous.

    Uses edit distance algorithm.

    Parameters
    ----------
    x : iterable
        First input iterable. Must be sequential and elements must also support '==' operator.
    y : iterable
        Second input iterable. Must be sequential and elements must also support '==' operator.
    empty_object : any, optional
        Empty object of the same class as x and y.
    append_func : function handle, optional
        Function that appends values to the end of the object of the same class as x and y.

    Returns
    -------
    out : iterable
        Longest common subsequence.

    Raises
    ------
    Exception
        'Please provide an empty object and the append operator.'
        If input isn't string or list, and the additional information isn't supplied.
    '''

    insert = Operation(cost=1, dx=0, dy=1)
    delete = Operation(cost=1, dx=1, dy=0)
    operations = [insert, delete]

    _, performed_operations = edit_distance_bu(x, y, operations)

    performed_operations.sort(key = lambda oij : oij[1])

    if type(x) is str:
        empty_object, append_func = '', str.__add__

    elif type(x) is list:
        empty_object, append_func = [], list.append

    if (empty_object is None) or (append_func is None):
        raise Exception('Please provide an empty object and the append operator.')

    subsequence = empty_object
    for operation, i, j in performed_operations:
        if (operation is not insert) and (operation is not delete):
            append_return_value = append_func(subsequence, x[i])
            if append_return_value is not None:
                subsequence = append_return_value

    return subsequence


# ### testing

# # on strings
# x = 'herllembo'
# y = 'chelilott'

# lcs = longest_common_subsequence(x,y)

# assert 'hello' == lcs

# # on lists
# x = [1,4,2,5,3]
# y = [1,0,2,3,4]

# lcs = longest_common_subsequence(x,y)

# assert [1,2,3] == lcs


# # on numpy arrays
# import numpy as np
# x = np.array([1,4,2,5,3])
# y = np.array([1,0,2,3,4])

# lcs = longest_common_subsequence(x, y, np.array([]), np.append)

# assert np.all(lcs == np.array([1,2,3]))

# print('Exiting...')