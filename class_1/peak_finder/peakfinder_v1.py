"""
Given a 1-dimensional array of integers, find a peak.

Position i is a peak if array[i-1] <= array[i] >= array[i+1].

The input is organized such that once the numbers start decreasing they cannot increase again. For example,
the following input is not valid because the values start decreasing at position 3, but then there is an increase in
position 5:

[0, 1, 2, 1, 1, 2, 1, 0]

On the other hand the following is valid:

[0, 1, 2, 1, 1, 0, -1, -2]

"""


def peak_finder(array):
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


def is_valid_idx(idx, array):
    return True if 0 <= idx < len(array) else False


if __name__ == '__main__':
    # expected 0
    print(peak_finder([1]))
    # expected 1
    print(peak_finder([1, 2]))
    # expected 0
    print(peak_finder([1, 0]))
    # expected 3
    print(peak_finder([0, 1, 2, 3, 3]))
    # expected 3
    print(peak_finder([0, 1, 2, 3, 2]))
    # expected 1
    print(peak_finder([0, 1, 1]))
    # expected 0
    print(peak_finder([0, 0]))
    # expected 2
    print(peak_finder([0, 1, 2, 1, 1, 0, -1, -2]))
