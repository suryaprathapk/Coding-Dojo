# 2nd April 2019, Problem level: Medium

# You are given an array of non-negative integers that represents a two-dimensional elevation map where each element is unit-width wall and the integer is the height. Suppose it will rain and all spots between two walls get filled up.

# Compute how many units of water remain trapped on the map in O(N) time and O(1) space.

# For example, given the input[2, 1, 2], we can hold 1 unit of water in the middle.

# Given the input[3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the second, and 3 in the fourth index(we cannot hold 5 since it would run off to the left), so we can trap 8 units of water.


def capacity(arr):
    n = len(arr)
    left_maxes = [0 for _ in range(n)]
    right_maxes = [0 for _ in range(n)]

    current_left_max = 0
    for i in range(n):
        current_left_max = max(current_left_max, arr[i])
        left_maxes[i] = current_left_max

    current_right_max = 0
    for i in range(n - 1, -1, -1):
        current_right_max = max(current_right_max, arr[i])
        right_maxes[i] = current_right_max

    total = 0
    for i in range(n):
        total += min(left_maxes[i], right_maxes[i]) - arr[i]
    return total