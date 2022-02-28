'''
Brady Neeb
<bneeb@mail.smcvt.edu>
'''
def gauss(A, n):
    ''' Implementation of Gauss Elimination in Python. A is the matrix, and n is the number of rows. '''

    for k in range(0, n):

        for i in range(k+1, n):

            entry_elim_col = i - 1
            elim_factor = -1 * A[i][entry_elim_col] / A[k][k]

            for j in range(0, n+1):

                A[i][j] = elim_factor * A[k][j] + A[i][j]

    return A


if __name__ == '__main__':

    A = [[1, 2, 13], [4, 5, 29]]
    n = 2
    print(gauss(A, n))
