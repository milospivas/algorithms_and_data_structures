''' Dynamic Programming: Parenthesization

    Optimal evaluation of associative expression A[0]*A[1]*...*A[n-1]
    representing multiplication of rectangular matrices.

    Author: Miloš Pivaš
'''

### shared functions ###############################################################################

def cost_mm(shapes, B_shape):
    ''' Calculates the cost of computing a matrix multiplication.

    Cost of computing a schoolbook matrix multiplication on two matrices.
    For matrices of sizes mxn and nxp, it is m*n*p.

    Parameters
    ----------
    shapes : (int, int)
        The shape of the first matrix to be multiplied.
    B_shape : (int, int)
        The shape of the second matrix to be multiplied.

    Returns
    -------
    out : int
        The cost of computing the multiplication.
        (inf if the multiplication is impossible)
    '''

    if shapes[1] != B_shape[0]:
        return float('Inf')

    return shapes[0] * shapes[1] * B_shape[1]


def shape_of_product(shapes, start, stop):
    ''' Returns the shape of the matrix product of matrices with shapes shapes[start:stop]

    Parameters
    ----------
    shapes : list
        List of (int, int) tuples, representing shapes of matrices.
    start : int
        Index of the first matrix' shape.
    stop : int
        Index after the last matrix' shape.

    Returns
    -------
    out : (int, int)
        The shape of the matrix product.
    '''

    return (shapes[start][0], shapes[stop-1][1])


def shapes_of_products(shapes, start, mid, stop):
    ''' Returns the shapes of matrix products of matrices
    with shapes shapes[start:mid] and shapes[mid:stop]

    Parameters
    ----------
    shapes : list
        List of (int, int) tuples, representing shapes of matrices.
    start : int
        Index of the first matrix' shape.
    mid : int
        Index of the middle matrix' shape.
    stop : int
        Index after the last matrix' shape.

    Returns
    -------
    out : (int, int), (int, int)
        Shapes of left and right matrix products.
    '''

    shape_L = shape_of_product(shapes, start, mid)
    shape_R = shape_of_product(shapes, mid, stop)
    return shape_L, shape_R


### Naive recursive DP #############################################################################

def parenthesize_nr(shapes):
    ''' Finds optimal way to parenthesize a matrix multiplication expression.

    Naive recursive method (without caching).

    Parameters
    ----------
    shapes : list
        List of (int, int) tuples, representing shapes of matrices.

    Returns
    -------
    out : list, int
        list
            Represents the order of multiplications via a list of indices.
        int
            Total cost of multiplication.
    '''

    def __parenthesize(start, stop):

        if len(shapes[start:stop]) <= 1:
            return [], 0

        min_cost = float('Inf')
        for mid in range(start+1, stop):
            indices_L, cost_L = __parenthesize(start, mid)
            indices_R, cost_R = __parenthesize(mid, stop)

            shape_L, shape_R = shapes_of_products(shapes, start, mid, stop)

            cost = cost_L + cost_R + cost_mm(shape_L, shape_R)

            if cost < min_cost:
                min_cost = cost
                min_indices_L = indices_L
                min_indices_R = indices_R
                min_index_mid = mid

        min_indices = min_indices_L + min_indices_R + [min_index_mid]

        return min_indices, min_cost

    start, stop = 0, len(shapes)
    sol = __parenthesize(start, stop)
    return sol


### Recursive DP with caching (memoization) ########################################################

def parenthesize_rc(shapes):
    ''' Finds optimal way to parenthesize a matrix multiplication expression.

    Recursive, dynamic programming method with caching (memoization).

    Parameters
    ----------
    shapes : list
        List of (int, int) tuples, representing shapes of matrices.

    Returns
    -------
    out : list, int
        list
            Represents the order of multiplications via a list of indices.
        int
            Total cost of multiplication.
    '''

    def __cache_init():
        cache = {}
        subarray_length = 1
        for start in range(len(shapes)):
            cache[start, start+subarray_length] = [], 0
        return cache

    def __find_optimal_midpoint(start, stop):
        min_cost = float('Inf')
        for mid in range(start+1, stop):
            indices_L, cost_L = __parenthesize_witch_caching(start, mid)
            indices_R, cost_R = __parenthesize_witch_caching(mid, stop)

            shape_L, shape_R = shapes_of_products(shapes, start, mid, stop)

            cost = cost_L + cost_R + cost_mm(shape_L, shape_R)

            if cost < min_cost:
                min_cost = cost
                min_indices_L = indices_L
                min_indices_R = indices_R
                min_index_mid = mid

        min_indices = min_indices_L + min_indices_R + [min_index_mid]

        return min_indices, min_cost


    def __parenthesize_witch_caching(start, stop):

        if (start, stop) in cache:
            return cache[start, stop]

        min_indices, min_cost = __find_optimal_midpoint(start, stop)

        cache[start, stop] = min_indices, min_cost

        return min_indices, min_cost


    if len(shapes) <= 1:
        return [], 0

    cache = __cache_init()
    sol = __parenthesize_witch_caching(start = 0, stop = len(shapes))
    return sol


### Iterative, bottom-up DP with caching (memoization) #############################################

def parenthesize_bu(shapes):
    ''' Finds optimal way to parenthesize a matrix multiplication expression.

    Iterative, bottom-up, dynamic programming method with caching (memoization).

    Parameters
    ----------
    shapes : list
        List of (int, int) tuples, representing shapes of matrices.

    Returns
    -------
    out : list, int
        list
            Represents the order of multiplications via a list of indices.
        int
            Total cost of multiplication.
    '''

    def __cache_init():
        cache = {}
        subarray_length = 1
        for start in range(len(shapes)):
            cache[start, start+subarray_length] = [], 0
        return cache

    def __get_topological_order_of_indices():
        for subarray_length in range(2, len(shapes)+1):
            number_of_subarrays = len(shapes) - subarray_length + 1
            for start in range(number_of_subarrays):
                stop = start + subarray_length
                yield start, stop

    def __find_optimal_midpoint(start, stop):
        min_cost = float('Inf')
        for mid in range(start+1, stop):
            indices_L, cost_L = cache[start, mid]
            indices_R, cost_R = cache[mid, stop]

            shape_L, shape_R = shapes_of_products(shapes, start, mid, stop)

            cost = cost_L + cost_R + cost_mm(shape_L, shape_R)

            if cost < min_cost:
                min_cost = cost
                min_indices_L = indices_L
                min_indices_R = indices_R
                min_index_mid = mid

        min_indices = min_indices_L + min_indices_R + [min_index_mid]

        return min_indices, min_cost

    if len(shapes) <= 1:
        return [], 0

    cache = __cache_init()
    topological_order_of_indices = __get_topological_order_of_indices()

    for start, stop in topological_order_of_indices:
        min_indices, min_cost = __find_optimal_midpoint(start, stop)
        cache[start, stop] = min_indices, min_cost

    return cache[0, len(shapes)]


### testing ########################################################################################

def test_parenthesization(shapes, true_indices, true_cost, parenthesize_func):
    ''' Tests parenthesize_func on shapes.

    Parameters
    ----------
    shapes : list
        List of (int, int) tuples, representing shapes of matrices.
    true_indices : list
        Represents the order of multiplications via a list of indices.
    true_cost : int
        Total cost of multiplication.
    parenthesize_func : function handle
        Parenthesization function to test.

    Returns
    -------
    out : bool
        Passed/Not passed the test.
    '''

    indices, cost = parenthesize_func(shapes)

    test_passed = (indices == true_indices) and (cost == true_cost)

    print('shapes:', shapes)
    print('product indices:', indices)
    print('cost:', cost)
    print('test_passed:', test_passed)
    return test_passed


for parenthesize_func in [parenthesize_nr, parenthesize_rc, parenthesize_bu]:
    help(parenthesize_func)

    shapes = [(2, 1), (1, 2), (2, 1)]
    true_indices = [2,1]
    true_cost = 4
    test_parenthesization(shapes, true_indices, true_cost, parenthesize_func)

    shapes = [(1, 2), (2, 1), (1, 2)]
    true_indices = [1,2]
    true_cost = 4
    test_parenthesization(shapes, true_indices, true_cost, parenthesize_func)

    shapes = [(1, 2), (2, 1)]
    true_indices = [1]
    true_cost = 2
    test_parenthesization(shapes, true_indices, true_cost, parenthesize_func)

    shapes = [(1, 2)]
    true_indices = []
    true_cost = 0
    test_parenthesization(shapes, true_indices, true_cost, parenthesize_func)

    shapes = []
    true_indices = []
    true_cost = 0
    test_parenthesization(shapes, true_indices, true_cost, parenthesize_func)

print('Exiting...')