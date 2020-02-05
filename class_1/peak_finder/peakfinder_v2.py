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

