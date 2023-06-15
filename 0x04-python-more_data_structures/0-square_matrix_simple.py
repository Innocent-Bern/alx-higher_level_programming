#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    rtn = []
    for i in range(len(matrix)):
        arr = []
        for x in range(len(matrix[i])):
            arr.append(matrix[i][x] * matrix[i][x])
        rtn.append(arr)
    return rtn
