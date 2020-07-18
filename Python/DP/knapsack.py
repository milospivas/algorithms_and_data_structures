''' Dynamic Programming: Knapsack
    N items have mass m[i], and value v[i].
    Find the optimal subset of items that maximize the total value,
    but whose total mass doesn't exceed the maximum carrying capacity of the knapsack - M.

    The problem is solvable in pseudopolynomial time O(N*M).
    It is pseudopolynomial because the input is given in O(N) + O(logM) space.
    (M is just a number - it is written in logM space).

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
    n : int, optional
        Current mass limit.
    i : int, optional
        Current item index.

    Returns
    -------
    out : float, list
        float - total accumulated value.
        list - items' indices.
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
    n : int, optional
        Current mass limit.
    i : int, optional
        Current item index.
    cache : dict, optional
        Hashmap of already computed solutions.

    Returns
    -------
    out : float, list
        float - total accumulated value.
        list - items' indices.
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


# Iterative, bottom-up variant with caching (memoization)

def knapsack_bu(m, v, M):
    ''' Maximise the value of a knapsack, given the items and mass limit.

    Iterative, bottom-up, dynamic programming method with caching.

    Parameters
    ----------
    m : list
        List of (int) masses of items.
    v : list
        List of (float/int) values of items.
    M : int
        Total mass limit of the knapsack.

    Returns
    -------
    out : float, list
        float - total accumulated value.
        list - items' indices.
    '''

    # cache init
    cache = {}
    for n in range(0, M+1):
        cache[(n, len(m))] = 0, []  # no items left, any mass
    for i in range(len(m)+1):
        cache[(0, i)] = 0, []       # no mass left, any items

    # topological order:
    # from smallest to largest size:
    for n in range(1, M+1):
        # from last to first item:
        for i in range(len(m)-1, -1, -1):

            # try excluding the item
            val_excl, indices_excl = cache[(n, i+1)]

            sol = val_excl, indices_excl

            # try including the item
            if n - m[i] >= 0:
                val_incl, indices_incl = cache[(n-m[i], i+1)]
                val_incl += v[i]

                if val_incl > val_excl:
                    sol = val_incl, indices_incl + [i]

            cache[(n, i)] = sol

    return cache[(M, 0)]


### testing

m = [1,2,3,4]
v = [1,2,3,42]
M = 5

for knapsack_func in [knapsack_nr, knapsack_rc, knapsack_bu]:
    help(knapsack_func)

    val, indices = knapsack_func(m, v, M)

    print('val:', val)
    print('indices:', indices)


print('Exiting...')