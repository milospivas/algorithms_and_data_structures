''' Dynamic Programming: Longest Common Subsequence

    Author: Miloš Pivaš
'''

from edit_distance import Operation
from edit_distance import edit_distance_bu

### using edit distance

def longest_common_subsequence(x, y):
    ''' Finds the longest common subsequence of given strings.

    Subsequence is sequential but doesn't have to be contiguous.
    Uses edit distance algorithm.

    Parameters
    ----------
    x : str
        First string.
    y : str
        Second string.

    Returns
    -------
    str
        Longest common subsequence.
    '''

    insert = Operation(1, 0, 1)
    delete = Operation(1, 1, 0)
    operations = [insert, delete]

    _, performed_operations = edit_distance_bu(x, y, operations)

    performed_operations.sort(key = lambda oij : oij[1])

    s = ''
    for o, i, j in performed_operations:
        if o is None:
            s += x[i]
    
    return s


### testing

x = 'herllembo'
y = 'chelilott'

x = ''.join(x.split(' '))
y = ''.join(y.split(' '))

lcs = longest_common_subsequence(x,y)

assert 'hello' == lcs

print('Exiting...')