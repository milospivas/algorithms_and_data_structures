''' Dynamic Programming: Longest Increasing Subsequence

    Depends on: longest_common_subsequence.py

    Author: Miloš Pivaš
'''

from longest_common_subsequence import longest_common_subsequence


def longest_increasing_subsequence(a, sort_func = None, empty_object = None, append_func = None, is_inplace = None):
    ''' Returns longest increasing subsequence (LIS) of the given iterable.

    Subsequence doesn't have to be made out of contiguous elements.
    Uses longest common subsequence with the sorted input.

    Parameters
    ----------
    a : iterable
        Input iterable. Must be sequential and elements must also support '==' operator.
    [sort_func : function handle]
        Function that sorts the input iterable.
    [empty_object : any]
        Empty object of the same class as x and y.
    [append_func : function handle]
        Function that appends values to the end of the object of the same class as x and y.
    [is_inplace : bool]
        Type of the append function. True if it operates in-place, False otherwise.

    Returns
    -------
    iterable
        Longest increasing subsequence.

    Raises
    ------
    Exception
        'Please provide the sort function.'
        If type(a) isn't str or list and sort_func isn't given.
    '''

    if type(a) is str:
        a_list = [x for x in a]
        a_list.sort()
        a_sorted = ''.join(a_list)
        sol = longest_common_subsequence(a, a_sorted)

    elif type(a) is list:
        a_sorted = sorted(a)
        sol = longest_common_subsequence(a, a_sorted)

    else:
        if (sort_func is None):
            raise Exception('Please provide the sort function.')
        a_sorted = sort_func(a)
        sol = longest_common_subsequence(a, a_sorted, empty_object, append_func, is_inplace)

    return sol


### Naive recursive (no caching)

def longest_increasing_subsequence_nr(a):
    ''' Returns longest increasing subsequence (LIS) of the given list.

    Subsequence doesn't have to be made out of contiguous elements.

    Parameters
    ----------
    a : str
        Input string.

    Returns
    -------
    str
        Longest increasing subsequence.
    '''

    def lis_nr(a, i = 0, prev = '\0'):
        ''' Returns longest increasing subsequence (LIS)* of the given list.

        Subsequence doesn't have to be made out of contiguous elements.
        *The subsequence is returned in reversed order

        Parameters
        ----------
        a : str
            Input string.
        [i : int]
            Index of the first element from which to start computing the LIS.
        [prev : str]
            Previous included element in the list (current maximum).

        Returns
        -------
        str
            Longest increasing subsequence *in reversed order.
        '''

        if i == len(a):
            return ''

        # try excluding the current element
        list_excl = lis_nr(a, i+1, prev)
        sol = list_excl

        # try including the current element
        if a[i] >= prev:
            list_incl = lis_nr(a, i+1, a[i])
            list_incl += a[i]

            if len(list_incl) > len(sol):
                sol = list_incl

        return sol

    sol_rev = lis_nr(a)
    sol = sol_rev[::-1]

    return sol


# # a = '131231'

# # for lis_func in [longest_increasing_subsequence, longest_increasing_subsequence_nr]:

# #     lis = lis_func(a)

# #     print(lis)

# a = '131231'
# lis = longest_increasing_subsequence(a)
# print(lis)

# a = [1,3,1,2,3,1]
# lis = longest_increasing_subsequence(a)
# print(lis)

# import numpy as np
# a = np.array([1,3,1,2,3,1])
# lis = longest_increasing_subsequence(a, np.sort, np.array([]), np.append, False)
# print(lis)

# print('Exiting...')





