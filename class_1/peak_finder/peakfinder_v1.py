"""
Given a 1-dimensional array of integers, find a peak.

Position i is a peak if array[i-1] <= array[i] >= array[i+1].

The input is organized such that once the numbers start decreasing they cannot increase again. For example,
the following input is not valid because the values start decreasing at position 3, but then there is an increase in
position 5:

[0, 1, 2, 1, 1, 2, 1, 0]

On the other hand the following is valid:

[0, 1, 2, 1, 1, 0, -1, -2]

With this constraint and definition of peak there is always at least one peak.
"""


# O(n)
def peak_finder_straightforward(array):
    if len(array) == 1:
        return 0

    for i in range(len(array)):
        if is_valid_idx(i-1, array):
            if is_valid_idx(i+1, array):
                if array[i-1] <= array[i] >= array[i+1]:
                    return i
            elif array[i-1] <= array[i]:
                return i
        elif array[i] >= array[i+1]:
            return i


# O(log_2 n) == O(log n)
def peak_finder_divide_n_conquer(idx, array):
    if is_valid_idx(idx - 1, array) and array[idx - 1] > array[idx]:
        return peak_finder_divide_n_conquer(int((idx - 1) / 2), array)
    elif is_valid_idx(idx + 1, array) and array[idx + 1] > array[idx]:
        return peak_finder_divide_n_conquer(int((idx + 1 + len(array)) / 2), array)
    else:
        return idx


def is_valid_idx(idx, array):
    return True if 0 <= idx < len(array) else False


if __name__ == '__main__':
    print("\nExpected: " + str(0))
    array = [1]
    print("Straightforward: " + str(peak_finder_straightforward(array)))
    print("Divide and conquer: " + str(peak_finder_divide_n_conquer(int(len(array) / 2), array)))

    print("\nExpected: " + str(1))
    array = [1, 2]
    print("Straightforward: " + str(peak_finder_straightforward(array)))
    print("Divide and conquer: " + str(peak_finder_divide_n_conquer(int(len(array) / 2), array)))

    print("\nExpected: " + str(0))
    array = [1, 0]
    print("Straightforward: " + str(peak_finder_straightforward(array)))
    print("Divide and conquer: " + str(peak_finder_divide_n_conquer(int(len(array) / 2), array)))

    print("\nExpected: " + str(3) + " or " + str(4))
    array = [0, 1, 2, 3, 3]
    print("Straightforward: " + str(peak_finder_straightforward(array)))
    print("Divide and conquer: " + str(peak_finder_divide_n_conquer(int(len(array) / 2), array)))

    print("\nExpected: " + str(3))
    array = [0, 1, 2, 3, 2]
    print("Straightforward: " + str(peak_finder_straightforward(array)))
    print("Divide and conquer: " + str(peak_finder_divide_n_conquer(int(len(array) / 2), array)))

    print("\nExpected: " + str(1) + " or " + str(2))
    array = [0, 1, 1]
    print("Straightforward: " + str(peak_finder_straightforward(array)))
    print("Divide and conquer: " + str(peak_finder_divide_n_conquer(int(len(array) / 2), array)))

    print("\nExpected: " + str(0) + " or " + str(1))
    array = [0, 0]
    print("Straightforward: " + str(peak_finder_straightforward(array)))
    print("Divide and conquer: " + str(peak_finder_divide_n_conquer(int(len(array) / 2), array)))

    print("\nExpected: " + str(2) + " or " + str(4))
    array = [0, 1, 2, 1, 1, 0, -1, -2]
    print("Straightforward: " + str(peak_finder_straightforward(array)))
    print("Divide and conquer: " + str(peak_finder_divide_n_conquer(int(len(array) / 2), array)))
