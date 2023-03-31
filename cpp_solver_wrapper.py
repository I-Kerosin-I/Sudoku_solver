import ctypes
from typing import List


def cpp_solver(sudoku: List[int]) -> list[int]:
    arr = (ctypes.c_short * 81)(*sudoku)
    res = (ctypes.c_short * 81)()

    func = ctypes.CDLL('./solver.dll').solver
    func.restype = ctypes.POINTER(ctypes.c_short * 81)

    return [i for i in func(arr, 0, 0, res).contents]
