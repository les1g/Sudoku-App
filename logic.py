# logic_test.py
from dokusan import generators, solvers # for generating and solving Sudoku puzzles
from dokusan.boards import BoxSize, Sudoku # for defining Sudoku board size and structure
import numpy as np # for handling arrays and reshaping

def generate_sudoku():
    """Generate a random Sudoku puzzle with an average rank of 150."""
    puzzle_str = str(generators.random_sudoku(avg_rank=200)) # Generate a Sudoku puzzle as a string
    arr = np.array([int(ch) for ch in puzzle_str]).reshape((9, 9)) # Convert string to a 9x9 NumPy array of integers
    return arr.tolist() # Returns a 9x9 list of lists of integers

def solve_sudoku(unsolved_sudoku):
    """Solve the given Sudoku puzzle."""
    sudoku = Sudoku.from_list(unsolved_sudoku, box_size=BoxSize(3, 3)) # Create a Sudoku object from the unsolved puzzle
    
    arr = np.array(list(str(solvers.backtrack(sudoku)))) # Convert the solved Sudoku to a NumPy array of integers
    return arr.reshape((9, 9)) # Returns the solved Sudoku as a 9x9 NumPy array

def format_as_numpy_grid(sudoku_list):
    """Convert a list-of-lists Sudoku puzzle to a 9x9 NumPy int array."""
    return np.array(sudoku_list, dtype=int).reshape((9, 9)) # Convert to a 9x9 NumPy array of integers
    
if __name__ == "__main__":
    print("hi")
    
    
