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

