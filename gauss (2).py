''' Brady Neeb 
    Gauss implementation in Python.
'''


def gauss(A, num_rows, num_cols):

    for k in range(0, num_rows-1):

        for i in range(k+1, num_rows):  # Row that will be changed

            pivot_mult = A[i][k]/A[k][k]

            for j in range(0, num_cols):  # Column number in that row

                A[i][j] = A[i][j] - pivot_mult*A[k][j]

    print("solution is: ", A)


if __name__ == '__main__':

    A = [[1, 2, 3, 4],
         [3, 0, 2, 1],
         [2, -1, 5, 1]]

    num_rows = len(A)
    num_cols = len(A[0])

    gauss(A, num_rows, num_cols)
