import numpy as np

EMPTY_CELL = -1

def check_valid_grid(puzzle: np.ndarray[tuple[int, int], np.dtype[np.uint8]]) -> bool:
    """
    stop at first violation and return - This is going to be used within the generator,
    simple to know whether or not this state satisfies the puzzle constraints
    Since we run this every time we generate a state, the expected number of
    conflicts should stay around 1 the entire time.
    """


def generate_puzzle(filled_in: np.uint8) -> np.ndarray[tuple[int, int], np.dtype[np.uint8]]:
    pass
