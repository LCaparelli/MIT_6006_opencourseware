"""
Given a 2-dimensional array of integers, find a peak.

Position [i][j] is a peak if and only if:

  - array[i-1][j] <= array[i][j]
    AND
  - array[i][j-1] <= array[i][j]
    AND
  - array[i+1][j] <= array[i][j]
    AND
  - array[i][j+1] <= array[i][j]

With this constraint and definition of peak there is always at least one peak.
"""


def larger_neighbor(i, j, matrix, largest_neighbor):
    return is_valid_pos(i, j, matrix) and matrix[i][j] >= largest_neighbor


def is_valid_pos(i, j, matrix):
    return 0 <= i < len(matrix) and 0 <= j < len(matrix[i])


def greedy_ascent(i, j, matrix):
    largest_neighbor_pos = (-1, -1)
    largest_neighbor = float('-inf')

    if larger_neighbor(i - 1, j, matrix, largest_neighbor):
        largest_neighbor = matrix[i - 1][j]
        largest_neighbor_pos = (i - 1, j)
    if larger_neighbor(i, j - 1, matrix, largest_neighbor):
        largest_neighbor = matrix[i][j - 1]
        largest_neighbor_pos = (i, j - 1)
    if larger_neighbor(i + 1, j, matrix, largest_neighbor):
        largest_neighbor = matrix[i + 1][j]
        largest_neighbor_pos = (i + 1, j)
    if larger_neighbor(i, j + 1, matrix, largest_neighbor):
        largest_neighbor = matrix[i][j + 1]
        largest_neighbor_pos = (i, j + 1)

    if largest_neighbor > matrix[i][j]:
        i, j = largest_neighbor_pos
        return greedy_ascent(i, j, matrix)
    else:
        return i, j


if __name__ == '__main__':
    print("\nExpected: " + str((2, 2)))
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print("Greedy ascent: " + str(greedy_ascent(0, 0, matrix)))

    print("\nExpected: " + str((2, 1)))
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 7]
    ]
    print("Greedy ascent: " + str(greedy_ascent(0, 0, matrix)))

    print("\nExpected: " + str((1, 1)))
    matrix = [
        [1, 2, 3],
        [4, 5, 4],
        [3, 2, 1]
    ]
    print("Greedy ascent: " + str(greedy_ascent(0, 0, matrix)))

    print("\nExpected: " + str((0, 0)))
    matrix = [
        [1]
    ]
    print("Greedy ascent: " + str(greedy_ascent(0, 0, matrix)))
