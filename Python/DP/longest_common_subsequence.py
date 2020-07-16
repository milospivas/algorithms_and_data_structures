''' Dynamic Programming: Longest Common Subsequence

    Depends on: edit_distance.py

    Author: Miloš Pivaš
'''

from edit_distance import Operation
from edit_distance import edit_distance_bu


def longest_common_subsequence(x, y, empty_object = None, append_func = None, is_inplace = None):
    ''' Finds the longest common subsequence in two given iterables.

    Subsequence is sequential but doesn't have to be contiguous.
    Uses edit distance algorithm.

    Parameters
    ----------
    x : iterable
        First input iterable. Must be sequential and elements must also support '==' operator.
    y : iterable
        Second input iterable. Must be sequential and elements must also support '==' operator.
    [empty_object : any]
        Empty object of the same class as x and y.
    [append_func : function handle]
        Function that appends values to the end of the object of the same class as x and y.
    [is_inplace : bool]
        Type of the append function. True if it operates in-place, False otherwise.

    Returns
    -------
    iterable
        Longest common subsequence.
    
    Raises
    ------
    Exception
        'Please provide an empty object, the append operator and its type.'
        If input isn't string or list, and the additional information isn't supplied.
    '''

    insert = Operation(1, 0, 1)
    delete = Operation(1, 1, 0)
    operations = [insert, delete]

    _, performed_operations = edit_distance_bu(x, y, operations)

    performed_operations.sort(key = lambda oij : oij[1])

    
    if type(x) is str:
        empty_object, append_func, is_inplace = '', str.__add__, False

    elif type(x) is list:
        empty_object, append_func, is_inplace = [], list.append, True
    
    if (empty_object is None) or (append_func is None) or (is_inplace is None):
        raise Exception('Please provide an empty object, the append operator and its type.')

    s = empty_object
    if is_inplace:
        for o, i, j in performed_operations:
            if o is None:
                append_func(s, x[i])
    else:
        for o, i, j in performed_operations:
            if o is None:
                s = append_func(s, x[i])

    return s


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

# lcs = longest_common_subsequence(x, y, np.array([]), np.append, False)

# assert np.all(lcs == np.array([1,2,3]))

# print('Exiting...')