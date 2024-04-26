from z3 import *

# Create a 2D array of 9x9 integer variables
X = [ [ Int("x_%s_%s" % (i+1, j+1)) for j in range(9) ]
      for i in range(9) ]

# Adding Model constrains
# Each cell contains a value in {1, ..., 9}
cells_c  = [ And(1 <= X[i][j], X[i][j] <= 9)
             for i in range(9) for j in range(9) ]

# Each row contains a digit at most once
rows_c   = [ Distinct(X[i]) for i in range(9) ]

# Each column contains a digit at most once
cols_c   = [ Distinct([ X[i][j] for i in range(9) ])
             for j in range(9) ]

# Each 3x3 square contains a digit at most once
sq_c     = [ Distinct([ X[3*i0 + i][3*j0 + j]
                        for i in range(3) for j in range(3) ])
             for i0 in range(3) for j0 in range(3) ]

# Combine all constrains into a single main constrain
sudoku_c = cells_c + rows_c + cols_c + sq_c

# sudoku instance, we use '0' for empty cells
# instance_exmaple = (
#     (0,0,0,0,9,4,0,3,0),
#     (0,0,0,5,1,0,0,0,7),
#     (0,8,9,0,0,0,0,4,0),
#     (0,0,0,0,0,0,2,0,8),
#     (0,6,0,2,0,1,0,5,0),
#     (1,0,2,0,0,0,0,0,0),
#     (0,7,0,0,0,0,5,2,0),
#     (9,0,0,0,6,5,0,0,0),
#     (0,4,0,9,7,0,0,0,0))

instance = (
    (0,0,0,0,6,1,0,0,2),
    (0,7,0,0,0,0,0,6,0),
    (9,2,0,0,0,0,0,0,0),
    (0,0,4,5,2,0,9,0,0),
    (0,8,2,1,0,4,6,3,0),
    (0,0,3,0,7,6,1,0,0),
    (0,0,0,0,0,0,0,9,8),
    (0,3,0,0,0,0,0,4,0),
    (6,0,0,3,8,0,0,0,0))

instance_c = [ If(instance[i][j] == 0,
                  True,
                  X[i][j] == instance[i][j])
               for i in range(9) for j in range(9) ]