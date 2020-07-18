''' Dynamic Programming: Longest Increasing Subsequence

    Depends on: longest_common_subsequence.py

    Author: Miloš Pivaš
'''

from longest_common_subsequence import longest_common_subsequence


def longest_increasing_subsequence(x, sort_func = None, empty_object = None, append_func = None):
    ''' Returns longest increasing subsequence (LIS) of the given iterable.

    Subsequence doesn't have to be made out of contiguous elements.
    Uses longest common subsequence with the sorted input.

    Works with iterables of any type, but, of course,
    in realistic use cases, this would be implemented as a class method,
    dedicated to specific type.

    Parameters
    ----------
    x : iterable
        Input iterable. Must be sequential and elements must also support '==' operator.
    sort_func : function handle, optional
        Function that sorts the input iterable.
    empty_object : any, optional
        Empty object of the same class as x and y.
    append_func : function handle, optional
        Function that appends values to the end of the object of the same class as x and y.

    Returns
    -------
    out : iterable
        Longest increasing subsequence.

    Raises
    ------
    Exception
        'Please provide the sort function.'
        If type(x) isn't str or list and sort_func isn't given.
    '''

    if type(x) is str:
        x_list = [x for x in x]
        x_list.sort()
        x_sorted = ''.join(x_list)
        sol = longest_common_subsequence(x, x_sorted)

    elif type(x) is list:
        x_sorted = sorted(x)
        sol = longest_common_subsequence(x, x_sorted)

    else:
        if (sort_func is None):
            raise Exception('Please provide the sort function.')
        x_sorted = sort_func(x)
        sol = longest_common_subsequence(x, x_sorted, empty_object, append_func)

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
    out : str
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
        i : int, optional
            Index of the first element from which to start computing the LIS.
        prev : str, optional
            Previous included element in the list (current maximum).

        Returns
        -------
        out : str
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
# lis = longest_increasing_subsequence(a, np.sort, np.array([]), np.append)
# print(lis)

# print('Exiting...')





