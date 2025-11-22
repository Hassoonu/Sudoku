import numpy as np
import Sudoku_Generator as S_GEN
import Sudoku_Solver as S_SLVR
# generates test cases for sudoku generator


def test_check_valid_grid():
    test_array_1 = np.array([
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0]])
    
    test_array_2 = np.array([
                           [1, 2, 3, 4, 5, 6, 7, 8, 9],
                           [7, 8, 9, 1, 2, 3, 4, 5, 6],
                           [4, 5, 6, 7, 8, 9, 1, 2, 3],
                           [9, 1, 2, 3, 4, 5, 6, 7, 8],
                           [6, 7, 8, 9, 1, 2, 3, 4, 5],
                           [3, 4, 5, 6, 7, 8, 9, 1, 2],
                           [8, 9, 1, 2, 3, 4, 5, 6, 7],
                           [5, 6, 7, 8, 9, 1, 2, 3, 4],
                           [2, 3, 4, 5, 6, 7, 8, 9, 1]
                           ])
    
    test_array_3 = np.array([
                           [1, 2, 3, 4, 5, 6, 7, 8, 9],
                           [7, 8, 9, 1, 2, 3, 4, 5, 6],
                           [4, 5, 6, 7, 8, 9, 1, 2, 3],
                           [9, 1, 2, 3, 4, 5, 6, 7, 8],
                           [6, 7, 8, 9, 1, 2, 3, 4, 5],
                           [3, 4, 5, 6, 7, 8, 9, 1, 2],
                           [2, 3, 4, 5, 6, 7, 8, 9, 1],
                           [8, 9, 1, 8, 9, 1, 2, 3, 4],
                           [2, 3, 4, 5, 6, 7, 8, 9, 1]
                           ])
    
    assert S_GEN.check_valid_grid(test_array_1) is False
    assert S_GEN.check_valid_grid(test_array_2) is True
    assert S_GEN.check_valid_grid(test_array_3) is False
    

def test_generate_puzzle():
    pass


if __name__ == "__main__":
    print("testing check_valid_grid...")

    test_check_valid_grid()

    print("testing generate_puzzle...")

    test_generate_puzzle()

    print("passed!")