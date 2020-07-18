''' Dynamic Programming: Parenthesization

    Optimal evaluation of associative expression A[0]*A[1]*...*A[n-1]
    representing multiplication of rectangular matrices.

    Author: Miloš Pivaš
'''


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


### Naive recursive DP

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

            shape_L, shape_R = shape_of_product(shapes, start, mid), shape_of_product(shapes, mid, stop)

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


### Recursive DP with caching (memoization)

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

    def __parenthesize(start, stop):

        if len(shapes[start:stop]) <= 1:
            return [], 0

        min_cost = float('Inf')
        for mid in range(start+1, stop):
            indices_L, cost_L = cache[start, mid] if (start, mid) in cache else __parenthesize(start, mid)
            indices_R, cost_R = cache[mid, stop] if (mid, stop) in cache else  __parenthesize(mid, stop)

            shape_L, shape_R = shape_of_product(shapes, start, mid), shape_of_product(shapes, mid, stop)

            cost = cost_L + cost_R + cost_mm(shape_L, shape_R)

            if cost < min_cost:
                min_cost = cost
                min_indices_L = indices_L
                min_indices_R = indices_R
                min_index_mid = mid

        min_indices = min_indices_L + min_indices_R + [min_index_mid]

        cache[start, stop] = min_indices, min_cost

        return min_indices, min_cost

    cache = {}
    start, stop = 0, len(shapes)
    sol = __parenthesize(start, stop)
    return sol


### Iterative, bottom-up DP with caching (memoization)

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
            for start in range(len(shapes) - subarray_length + 1):
                stop = start + subarray_length
                yield start, stop

    def __find_optimal_midpoint(start, stop):
        min_cost = float('Inf')
        for mid in range(start+1, stop):
            indices_L, cost_L = cache[start, mid]
            indices_R, cost_R = cache[mid, stop]

            shape_L, shape_R = shape_of_product(shapes, start, mid), shape_of_product(shapes, mid, stop)

            cost = cost_L + cost_R + cost_mm(shape_L, shape_R)

            if cost < min_cost:
                min_cost = cost
                min_indices_L = indices_L
                min_indices_R = indices_R
                min_index_mid = mid

        min_indices = min_indices_L + min_indices_R + [min_index_mid]

        return min_indices, min_cost

    cache = __cache_init()
    topological_order_of_indices = __get_topological_order_of_indices()

    for start, stop in topological_order_of_indices:
        min_indices, min_cost = __find_optimal_midpoint(start, stop)
        cache[start, stop] = min_indices, min_cost

    return cache[0, len(shapes)]


### testing
def test_parenthesization(shapes, parenthesize_func):
    ''' Tests parenthesize_func on shapes
    '''

    indices, cost = parenthesize_func(shapes)

    print('shapes:', shapes)
    print('product indices:', indices)
    print('cost:', cost)
    print()


for parenthesize_func in [parenthesize_nr, parenthesize_rc, parenthesize_bu]:
    help(parenthesize_func)

    shapes = [(2, 1), (1, 2), (2, 1)]
    test_parenthesization(shapes, parenthesize_func)

    shapes = [(1, 2), (2, 1), (1, 2)]
    test_parenthesization(shapes, parenthesize_func)

print('Exiting...')