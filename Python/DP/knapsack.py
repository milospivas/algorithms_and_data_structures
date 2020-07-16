''' Dynamic Programming: Knapsack
    N items have mass m[i], and value v[i].
    Find the optimal subset of items that maximize the total value,
    but whose total mass doesn't exceed the maximum carrying capacity of the knapsack - M.

    Author: Miloš Pivaš, student
'''


# Naive recursive variant

def knapsack_nr(m, v, M, n = None, i = 0):
    ''' Maximise the value of a knapsack, given the items and mass limit.

    Naive recursive variant (no caching).

    Parameters
    ----------
    m : list
        List of (int) masses of items.
    v : list
        List of (float/int) values of items.
    M : int
        Total mass limit of the knapsack.
    [n : int]
        Current mass limit.
    [i : int]
        Current item index.
    
    Returns
    -------
    (float, list)
        float - total accumulated value.
        list - items' indices
    '''

    if n is None:
        n = M

    if i == len(m):
        return 0, []
    
    # try excluding the item
    val_excl, indices_excl = knapsack_nr(m, v, M, n, i + 1)
    sol = val_excl, indices_excl

    # try including the item
    if n - m[i] >= 0:
        val_incl, indices_incl = knapsack_nr(m, v, M, n - m[i], i + 1)
        val_incl += v[i]

        if val_incl > val_excl:
            sol = val_incl, indices_incl + [i]
    
    return sol


# Recursive variant with caching (memoization)

def knapsack_rc(m, v, M, n = None, i = 0, cache = None):
    ''' Maximise the value of a knapsack, given the items and mass limit.

    Recursive DP method, with caching.

    Parameters
    ----------
    m : list
        List of (int) masses of items.
    v : list
        List of (float/int) values of items.
    M : int
        Total mass limit of the knapsack.
    [n : int]
        Current mass limit.
    [i : int]
        Current item index.
    [cache : dict]
        Hashmap of already computed solutions.
    
    Returns
    -------
    (float, list)
        float - total accumulated value.
        list - items' indices
    '''

    if n is None:
        n = M

    if i == len(m):
        return 0, []

    if cache is None:
        cache = {}

    # try excluding the item
    if (n, i+1) in cache:
        val_excl, indices_excl = cache[(n, i+1)]
    else:
        val_excl, indices_excl = knapsack_rc(m, v, M, n, i + 1, cache)

    sol = val_excl, indices_excl

    # try including the item
    if n - m[i] >= 0:
        if (n-m[i], i+1) in cache:
            val_incl, indices_incl = cache[(n-m[i], i+1)]
        else:
            val_incl, indices_incl = knapsack_rc(m, v, M, n - m[i], i + 1, cache)
            val_incl += v[i]

        if val_incl > val_excl:
            sol = val_incl, indices_incl + [i]
  
    cache[(n, i)] = sol
    return sol
    

### testing

m = [1,2,3,4]
v = [1,2,3,42]
M = 5

val, indices = knapsack_nr(m, v, M)

print('val:', val)
print('indices:', indices)


val, indices = knapsack_nr(m, v, M)

print('val:', val)
print('indices:', indices)


print('Exiting...')