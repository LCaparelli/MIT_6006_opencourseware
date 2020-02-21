"""
Given a 2-dimensional array of integers, find a peak.

Each row is organized such that once the numbers start decreasing they cannot increase again. For example,
the following row is not valid because the values start decreasing at position 3, but then there is an increase in
position 5:

[0, 1, 2, 1, 1, 2, 1, 0]

On the other hand the following is valid:

[0, 1, 2, 1, 1, 0, -1, -2]

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


# O(n)
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


def get_max_value_idx(col, matrix):
    largest = matrix[0][col]
    largest_idx = 0
    for row in range(1, len(matrix)):
        if matrix[row][col] > largest:
            largest = matrix[row][col]
            largest_idx = row

    return largest_idx


def divide_n_conquer(col, matrix):
    row = get_max_value_idx(col, matrix)

    if is_valid_pos(row, col - 1, matrix) and matrix[row][col - 1] > matrix[row][col]:
        return divide_n_conquer(int((col - 1) / 2), matrix)
    elif is_valid_pos(row, col + 1, matrix) and matrix[row][col + 1] > matrix[row][col]:
        return divide_n_conquer(int((col + 1 + len(matrix[row])) / 2), matrix)
    else:
        return row, col


if __name__ == '__main__':
    print("\nExpected: " + str((2, 2)))
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print("Greedy ascent: " + str(greedy_ascent(0, 0, matrix)))
    print("Divide and conquer: " + str(divide_n_conquer(int(len(matrix) / 2), matrix)))

    print("\nExpected: " + str((2, 1)))
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 7]
    ]
    print("Greedy ascent: " + str(greedy_ascent(0, 0, matrix)))
    print("Divide and conquer: " + str(divide_n_conquer(int(len(matrix) / 2), matrix)))

    print("\nExpected: " + str((1, 1)))
    matrix = [
        [1, 2, 3],
        [4, 5, 4],
        [3, 2, 1]
    ]
    print("Greedy ascent: " + str(greedy_ascent(0, 0, matrix)))
    print("Divide and conquer: " + str(divide_n_conquer(int(len(matrix) / 2), matrix)))

    print("\nExpected: " + str((0, 0)))
    matrix = [
        [1]
    ]
    print("Greedy ascent: " + str(greedy_ascent(0, 0, matrix)))
    print("Divide and conquer: " + str(divide_n_conquer(int(len(matrix) / 2), matrix)))
