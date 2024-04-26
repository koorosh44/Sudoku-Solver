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