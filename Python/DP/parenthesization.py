''' Dynamic Programming: Parenthesization

    Optimal evaluation of associative expression A[0]*A[1]*...*A[n-1]
    representing multiplication of rectangular matrices.

    Author: Miloš Pivaš
'''


def cost_mm(A_shape, B_shape):
    ''' Calculates the cost of computing a matrix multiplication.

    Cost of computing a schoolbook matrix multiplication on two matrices.
    For matrices of sizes mxn and nxp, it is m*n*p.

    Parameters
    ----------
    A_shape : (int, int)
        The shape of the first matrix to be multiplied.
    B_shape : (int, int)
        The shape of the second matrix to be multiplied.

    Returns
    -------
    out : int
        The cost of computing the multiplication.
        (inf if the multiplication is impossible)
    '''

    if A_shape[1] != B_shape[0]:
        return float('Inf')

    return A_shape[0] * A_shape[1] * B_shape[1]


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

def parenthesize_bu(A_shapes):
    ''' Finds optimal way to parenthesize a matrix multiplication expression.

    Iterative, bottom-up, dynamic programming method with caching (memoization).

    Parameters
    ----------
    A_shapes : list
        List of (int, int) tuples, representing shapes of matrices.

    Returns
    -------
    out : list, int
        list
            Represents the order of multiplications via a list of indices.
        int
            Total cost of multiplication.
    '''

    N = len(A_shapes)

    # cache init
    cache = {}
    for i in range(N):
        cache[(i, i+1)] = ([], 0)

    # for each subsequence length bigger than 1
    for n in range(2, N+1):
        # for each starting index of the subsequence
        for i in range(N - n + 1):
            # compute ending index
            j = i + n

            # find optimum point
            min_cost = float('Inf')
            for k in range(i+1, j):
                indices_l, cost_l = cache[(i, k)]
                indices_r, cost_r = cache[(k, j)]

                L_shape = (A_shapes[i][0], A_shapes[k-1][1])
                R_shape = (A_shapes[k][0], A_shapes[j-1][1])
                cost = cost_mm(L_shape, R_shape)

                cost += cost_l + cost_r

                if cost < min_cost:
                    min_cost = cost
                    min_index = k
                    min_indices_l = indices_l
                    min_indices_r = indices_r

            min_indices = min_indices_l + min_indices_r + [min_index]

            cache[(i, j)] = min_indices, min_cost

    return cache[(0, N)]


### testing
def test_parenthesization(A_shape, parenthesize_func):
    ''' Tests parenthesize_func on A_shape
    '''

    indices, cost = parenthesize_func(A_shape)

    print('shapes:', A_shape)
    print('product indices:', indices)
    print('cost:', cost)
    print()


for parenthesize_func in [parenthesize_nr, parenthesize_rc, parenthesize_bu]:
    help(parenthesize_func)

    A_shape = [(2, 1), (1, 2), (2, 1)]
    test_parenthesization(A_shape, parenthesize_func)

    A_shape = [(1, 2), (2, 1), (1, 2)]
    test_parenthesization(A_shape, parenthesize_func)

print('Exiting...')