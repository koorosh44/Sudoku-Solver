# Sudoku-Solver

## Overview
This script uses the Z3 theorem prover from Microsoft Research to solve Sudoku puzzles. The Z3 solver is a powerful tool that can solve many types of logical problems, including constraint satisfaction problems (CSPs) like Sudoku.

## Dependencies
- Python 3
- Z3 Solver library for Python

You can install the Z3 Solver library using pip:
```bash
pip install z3-solver
```

## Usage
To use this script, you need to define your Sudoku puzzle as a 9x9 tuple of tuples, where 0 represents an empty cell. For example:

```python
instance = (
    (0,0,0,0,9,4,0,3,0),
    (0,0,0,5,1,0,0,0,7),
    (0,8,9,0,0,0,0,4,0),
    (0,0,0,0,0,0,2,0,8),
    (0,6,0,2,0,1,0,5,0),
    (1,0,2,0,0,0,0,0,0),
    (0,7,0,0,0,0,5,2,0),
    (9,0,0,0,6,5,0,0,0),
    (0,4,0,9,7,0,0,0,0))
```

Then, run the script. If the puzzle is solvable, the script will print the solved puzzle. If the puzzle is not solvable, it will print "failed to solve".

## How It Works
The script first creates a 9x9 matrix of integer variables, each representing a cell in the Sudoku puzzle. It then defines the constraints of the Sudoku puzzle: each cell must contain a value between 1 and 9, each row must contain distinct values, each column must contain distinct values, and each 3x3 square must contain distinct values. These constraints are added to a Z3 solver. The solver checks if there is an assignment of values to the variables that satisfies all the constraints. If such an assignment exists, the solver returns it as the solution to the Sudoku puzzle.

## Limitations
This script can only solve standard 9x9 Sudoku puzzles. It cannot solve variations of Sudoku such as 16x16 puzzles, diagonal Sudoku, etc.

## License
This script is released under the MIT license. You are free to use, modify, and distribute the script as long as you include the original copyright notice and disclaimer.
