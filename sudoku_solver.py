from copy import deepcopy
import time

sudoku_hard = [[0, 0, 5, 0, 0, 0, 7, 0, 0],
               [0, 0, 0, 4, 0, 0, 0, 9, 0],
               [2, 0, 0, 0, 7, 0, 0, 0, 3],
               [0, 9, 0, 0, 0, 4, 0, 0, 0],
               [0, 0, 1, 0, 8, 0, 2, 0, 0],
               [0, 0, 0, 5, 0, 0, 0, 6, 0],
               [8, 0, 0, 0, 2, 0, 0, 0, 1],
               [0, 6, 0, 0, 0, 9, 0, 0, 0],
               [0, 0, 4, 0, 0, 0, 8, 0, 0]]

sudoku_easy = [[8, 0, 0, 3, 0, 0, 0, 2, 0],
               [0, 4, 5, 2, 0, 9, 6, 0, 8],
               [0, 3, 0, 7, 0, 0, 0, 0, 5],
               [0, 6, 3, 0, 5, 0, 7, 0, 0],
               [5, 0, 0, 0, 9, 7, 0, 6, 0],
               [0, 0, 7, 0, 3, 6, 8, 5, 0],
               [0, 9, 8, 0, 0, 1, 0, 7, 4],
               [0, 0, 4, 6, 0, 3, 0, 8, 2],
               [0, 7, 0, 9, 0, 0, 0, 0, 0]]

sudoku_solved = [[2, 9, 3, 4, 5, 7, 6, 8, 1],
                 [4, 7, 5, 1, 8, 6, 3, 9, 2],
                 [1, 6, 8, 3, 9, 2, 7, 4, 5],
                 [9, 4, 2, 5, 7, 1, 8, 6, 3],
                 [3, 8, 1, 6, 2, 9, 5, 7, 4],
                 [6, 5, 7, 8, 3, 4, 1, 2, 9],
                 [7, 2, 6, 9, 1, 3, 4, 5, 8],
                 [5, 1, 4, 2, 6, 8, 9, 3, 7],
                 [8, 3, 9, 7, 4, 5, 2, 0, 0]]


def solver(sud, x=0, y=0):
    sudoku = deepcopy(sud)
    res = None
    if sudoku[y][x] == 0:
        field3x3 = []
        for i in range(3):
            for j in range(3):
                if (element := sudoku[y - y % 3 + i][x - x % 3 + j]) != 0:
                    field3x3.append(element)

        for digit in range(1, 10):
            if digit not in sudoku[y] and \
                    digit not in [sudoku[i][x] for i in range(9)] and \
                    digit not in field3x3:
                sudoku[y][x] = digit
                if not (x == 8 and y == 8):
                    res = solver(sudoku, (x + 1) % 9, y + (x + 1) // 9)
                    if res is not None:
                        return res
                else:
                    return sudoku

    elif not (x == 8 and y == 8):
        res = solver(sudoku, (x + 1) % 9, y + (x + 1) // 9)
    else:
        return sudoku

    return res


if __name__ == '__main__':
    start_time = time.time()
    result = solver(sudoku_hard)
    print(f"--- {time.time() - start_time} seconds ---")
    for k in range(9):
        print(result[k], '\n')
