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

def knapsack_nr(masses, values, mass_limit):
    ''' Maximise the value of a knapsack, given the items and mass limit.

    Naive recursive variant (no caching).

    Parameters
    ----------
    masses : list
        List of (int) masses of items.
    values : list
        List of (float/int) values of items.
    mass_limit : int
        Total mass limit of the knapsack.

    Returns
    -------
    out : float, list
        float - total accumulated value.
        list - items' indices.
    '''

    def __knapsack(curr_mass_limit = mass_limit, curr_idx = 0):

        if curr_idx == len(masses):
            return 0, []

        # try excluding the current item
        val_excluding, indices_excluding = __knapsack(curr_mass_limit, curr_idx + 1)

        # try including the current item
        next_mass_limit = curr_mass_limit - masses[curr_idx]
        if next_mass_limit >= 0:
            val_including, indices_including = __knapsack(next_mass_limit, curr_idx + 1)
            val_including += values[curr_idx]
            indices_including += [curr_idx]
        else:
            val_including, indices_including = -float('Inf'), []

        sol = (val_including, indices_including) if (val_including > val_excluding) else (val_excluding, indices_excluding)

        return sol

    sol = __knapsack()
    return sol


# Recursive variant with caching (memoization)

def knapsack_rc(masses, values, mass_limit):
    ''' Maximise the value of a knapsack, given the items and mass limit.

    Recursive DP method, with caching.

    Parameters
    ----------
    masses : list
        List of (int) masses of items.
    values : list
        List of (float/int) values of items.
    mass_limit : int
        Total mass limit of the knapsack.

    Returns
    -------
    out : float, list
        float - total accumulated value.
        list - items' indices.
    '''

    def __knapsack_with_caching(curr_mass_limit = mass_limit, curr_idx = 0):

        if curr_idx == len(masses):
            return 0, []

        # try excluding the current item
        val_excluding, indices_excluding = cache[curr_mass_limit, curr_idx + 1] if (curr_mass_limit, curr_idx+1) in cache else __knapsack_with_caching(curr_mass_limit, curr_idx+1)

        # try including the current item
        next_mass_limit = curr_mass_limit - masses[curr_idx]
        if next_mass_limit >= 0:
            val_including, indices_including = cache[next_mass_limit, curr_idx + 1] if (next_mass_limit, curr_idx+1) in cache else __knapsack_with_caching(next_mass_limit, curr_idx+1)
            val_including += values[curr_idx]
            indices_including += [curr_idx]
        else:
            val_including, indices_including = -float('Inf'), []

        sol = (val_including, indices_including) if (val_including > val_excluding) else (val_excluding, indices_excluding)

        cache[curr_mass_limit, curr_idx] = sol

        return sol

    cache = {}
    sol = __knapsack_with_caching()
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