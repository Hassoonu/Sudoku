import numpy as np

EMPTY_CELL = -1

def check_valid_grid(puzzle: np.ndarray[tuple[int, int], np.dtype[np.uint8]]) -> bool:
    """
    stop at first violation and return - This is going to be used within the generator,
    simple to know whether or not this state satisfies the puzzle constraints
    Since we run this every time we generate a state, the expected number of
    conflicts should stay around 1 the entire time.
    """
    rows, cols = puzzle.shape
    for curr_col in range(cols):
        for curr_row in range(rows):
            total_row = (puzzle[curr_row, :]).flatten()
            total_col = (puzzle[:, curr_col]).flatten()

            grid_x_high, grid_y_high = curr_col//3, curr_row % 3
            grid_x_low = (curr_col-1)//3 if (curr_col > 0) else 0
            grid_y_low = (curr_row-1) % 3 if (curr_row > 0) else 0
 
            curr_grid = (puzzle[grid_y_low:grid_y_high, grid_x_low:grid_x_high]).flatten()

            if(total_row.size != np.unique(total_row).size):
                return False # non-unique nums exist if difference in sizes
            if(total_col.size != np.unique(total_col).size):
                return False # non-unique nums exist if difference in sizes
            if(curr_grid.size != np.unique(curr_grid).size):
                return False # non-unique nums exist if difference in sizes
            
    return True


def generate_puzzle(filled_in: np.uint8) -> np.ndarray[tuple[int, int], np.dtype[np.uint8]]:

    new_puzzle = np.zeros((9,9), dtype=np.uint8)

    rows, columns = new_puzzle.shape

    for row in rows:
        for col in columns:
            pass

"""
This is significantly more complex — but also more impressive and educational.
You are essentially describing SAT/CSP-driven constructive generation.

# Terminology you’ll want to research:

The topic is often discussed under names like:

* Latin square constructive generation
* Exact cover / DLX generation without completion
* Constraint-directed puzzle synthesis
* Incremental generation with uniqueness enforcement
* CSP constructive search (opposite of generate-and-prune)

You are looking for generator algorithms that:

* construct the puzzle row by row or cell by cell, guided by constraints
* ensure that every placement leaves at least one valid solution
* enforce uniqueness early or periodically to avoid wasted effort

Good search terms for papers / resources:

* "constraint guided sudoku generation"
* "uniqueness-preserving sudoku generation"
* "sudoku puzzle synthesis CSP"
* "incremental sudoku generator exact cover"
* "latin square constructive generator"


Look particularly for resources that mention:

* DLX (Knuth, Dancing Links)
* polytime constructive generation for Latin squares
* CSP-based puzzle synthesis
* Direct Sudoku generation (not generate-then-remove) is rare but respected.

"""