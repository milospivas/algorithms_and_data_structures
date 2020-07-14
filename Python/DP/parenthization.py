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
    int
        The cost of computing the multiplication.
        (inf if the multiplication is impossible)
    '''

    if A_shape[1] != B_shape[0]:
        return float('Inf')
    
    return A_shape[0] * A_shape[1] * B_shape[1]


### Naive recursive DP

def parenthesize_nr(A_shapes, i = 0, j = None):
    ''' Finds optimal way to parenthesize a matrix multiplication expression.

    Parameters
    ----------
    A_shapes : list
        List of (int, int) tuples, representing shapes of matrices.
    [i : int]
        Index of the first matrix in the expression.
    [j : int]
        Index of the last matrix in the expression.

    Returns
    -------

    '''

    if j is None:
        j = len(A_shapes)
    
    if i == j:
        return [], 0

    if i == j-1:
        return [], 0
    
    min_cost = float('Inf')

    for k in range(i+1, j):
        indices_l, cost_l = parenthesize_nr(A_shapes, i, k)
        indices_r, cost_r = parenthesize_nr(A_shapes, k, j)

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
    
    return min_indices, min_cost


### testing
A_shape = [(2, 1), (1, 2), (2, 1)]

indices, cost = parenthesize_nr(A_shape)

print('shapes:', A_shape)
print('product indices:', indices)
print('cost:', cost)
print()

A_shape = [(1, 2), (2, 1), (1, 2)]

indices, cost = parenthesize_nr(A_shape)

print('shapes:', A_shape)
print('product indices:', indices)
print('cost:', cost)
print()

print('Exiting...')