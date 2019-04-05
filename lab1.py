# Sajan Johal
# Lab 1 Part 1


def max_list_iter(int_list):
    """finds the max of a list of numbers and returns the value (not the index)
    If int_list is empty, returns None. If list is Non, raises ValueError"""

    if int_list == []:
        return None
    elif int_list is None:
        raise ValueError

    max_val = -1000000000000
    for i in range(len(int_list)):
        if int_list[i] == list:
            for j in range(len(int_list[i])):
                if int_list[i][j] > max_val:
                    max_val = int_list[i][j]
        else:
            if int_list[i] > max_val:
                max_val = int_list[i]
    return max_val


def reverse_rec(input_list):
    """recursively reverses a list of numbers and returns the reversed list
    If list is None, raises ValueError"""

    if not input_list:
        return []
    return [input_list[-1]] + reverse_rec(input_list[:-1])


def bin_search(target, low, high, int_list):  # must use recursion
    """searches for target in int_list[low:high] and returns index if found
    If target is not found returns None. If list is None, raises ValueError """

    if not low < high:
        raise ValueError
    mid = (high + low)//2
    if int_list[mid] < target:
        return bin_search(target, mid + 1, high, int_list)
    elif int_list[mid] > target:
        return bin_search(target, low, mid, int_list)
    else:
        return mid