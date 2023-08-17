#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squares = []
    for row in matrix:
        new_row = []
        for item in row:
            new_row.append(item ** 2)
        squares.append(new_row)
    return (squares)
