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


a = '132231'

for lis_func in [longest_increasing_subsequence]:

    lis = lis_func(a)

    print(lis)

print('Exiting...')


    


