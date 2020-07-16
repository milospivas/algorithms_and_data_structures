''' Dynamic Programming: Longest Increasing Subsequence

    Depends on: longest_common_subsequence.py

    Author: Miloš Pivaš
'''

from longest_common_subsequence import longest_common_subsequence


def longest_increasing_subsequence(a):
    ''' Returns longest increasing subsequence (LIS) of the given list.

    Subsequence doesn't have to be made out of contiguous elements.
    Uses longest common subsequence with the sorted input.
    
    Parameters
    ----------
    a : str
        Input string.
    
    Returns
    -------
    list
        Longest increasing subsequence.
    '''

    a_list = [x for x in a]
    a_list.sort()
    a_sorted = ''.join(a_list)

    return longest_common_subsequence(a, a_sorted)


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


a = '131231'

for lis_func in [longest_increasing_subsequence, longest_increasing_subsequence_nr]:

    lis = lis_func(a)

    print(lis)

print('Exiting...')


    


