''' Dynamic Programming: Knapsack
    N items have mass m[i], and value v[i].
    Find the optimal subset of items that maximize the total value,
    but whose total mass doesn't exceed the maximum carrying capacity of the knapsack - M.

    The problem is solvable in pseudopolynomial time O(N*M).
    It is pseudopolynomial because the input is given in O(N) + O(logM) space.
    (M is just a number - it is written in logM space).

    Author: Miloš Pivaš, student
'''


### Naive recursive variant  ##################################################################################################

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

        if curr_mass_limit == 0 or curr_idx == len(masses):
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


### Recursive variant with caching (memoization)  #############################################################################

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

    def __cache_init():
        cache = {}
        for curr_mass_limit in range(0, mass_limit+1):
            cache[curr_mass_limit, len(masses)] = 0, [] # any mass, no items left
        for curr_idx in range(len(masses)+1):
            cache[0, curr_idx] = 0, []                  # no mass left, any items
        return cache

    def __knapsack_with_caching(curr_mass_limit = mass_limit, curr_idx = 0):

        if (curr_mass_limit, curr_idx) in cache:
            return cache[curr_mass_limit, curr_idx]

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

    cache = __cache_init()
    sol = __knapsack_with_caching()
    return sol


### Iterative, bottom-up variant with caching (memoization) ###################################################################

def knapsack_bu(masses, values, mass_limit):
    ''' Maximise the value of a knapsack, given the items and mass limit.

    Iterative, bottom-up, dynamic programming method with caching.

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

    def __cache_init():
        cache = {}
        for curr_mass_limit in range(0, mass_limit+1):
            cache[curr_mass_limit, len(masses)] = 0, [] # any mass, no items left
        for curr_idx in range(len(masses)+1):
            cache[0, curr_idx] = 0, []                  # no mass left, any items
        return cache

    def __get_topological_order():
        for curr_mass_limit in range(1, mass_limit+1):
            for curr_idx in range(len(masses)-1, -1, -1):
                yield curr_mass_limit, curr_idx


    cache = __cache_init()

    topological_order = __get_topological_order()

    for curr_mass_limit, curr_idx in topological_order:

        # try excluding the current item
        val_excluding, indices_excluding = cache[curr_mass_limit, curr_idx + 1]

        # try including the current item
        next_mass_limit = curr_mass_limit - masses[curr_idx]
        if next_mass_limit >= 0:
            val_including, indices_including = cache[next_mass_limit, curr_idx + 1]
            val_including += values[curr_idx]
            indices_including += [curr_idx]
        else:
            val_including, indices_including = -float('Inf'), []

        sol = (val_including, indices_including) if (val_including > val_excluding) else (val_excluding, indices_excluding)

        cache[curr_mass_limit, curr_idx] = sol

    return cache[mass_limit, 0]


### testing ###################################################################################################################

masses = [1,2,3,4]
values = [1,2,3,42]
mass_limit = 5
true_val = 43
true_indices = [3,0]

for knapsack_func in [knapsack_nr, knapsack_rc, knapsack_bu]:
    help(knapsack_func)

    val, indices = knapsack_func(masses, values, mass_limit)

    test_passed = (val == true_val) and (indices == true_indices)

    print('val:', val)
    print('indices:', indices)
    print('test passed:', test_passed)


print('Exiting...')