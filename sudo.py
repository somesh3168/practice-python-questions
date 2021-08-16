import numpy as np
arr_zeros = np.zeros((9,9))
print(arr_zeros)
sudoku=(
    list([0 for _ in range(9)] for _ in range(9))
)
print(type(sudoku))
sudoku=np.array(sudoku)
print(type(sudoku))
print(sudoku)

# source: https://iq.opengenus.org/2d-array-in-numpy/