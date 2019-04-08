######################################

# Problem level – Easy

# Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.

# Recall that the median of an even-numbered list is the average of the two middle numbers.

# For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

# 2 1.5 2 3.5 2 2 2
######################################


def get_median(min_heap, max_heap):
    if len(min_heap) > len(max_heap):
        return min_heap.find_min()
    elif len(min_heap) < len(max_heap):
        return max_heap.find_max()
    else:
        min_root = min_heap.find_min()
        max_root = max_heap.find_max()
        return (min_root + max_root) / 2

def add(num, min_heap, max_heap):
    # If empty, then just add it to the max heap.
    if len(min_heap) + len(max_heap) <= 1:
        max_heap.insert(num)
        return

    median = get_median(min_heap, max_heap)
    if num > median:
        # add it to the min heap
        min_heap.insert(num)
    else:
        max_heap.insert(num)

def rebalance(min_heap, max_heap):
    if len(min_heap) > len(max_heap) + 1:
        root = min_heap.extract_min()
        max_heap.insert(root)
    elif len(max_heap) > len(min_heap) + 1:
        root = max_heap.extract_max()
        min_heap.insert(root)

def print_median(min_heap, max_heap):
    print(get_median(min_heap, max_heap))

def running_median(stream):
    min_heap = minheap()
    max_heap = maxheap()
    for num in stream:
        add(num, min_heap, max_heap)
        rebalance(min_heap, max_heap)
        print_median(min_heap, max_heap)