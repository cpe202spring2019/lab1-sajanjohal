# Sajan Johal
# Lab 1 Part 1


def max_list_iter(int_list):  # must use iteration not recursion
    if int_list == []:
        return None
    elif int_list is None:
        raise ValueError

    max_val = -10000000
    for i in range(len(int_list)):
        if int_list[i] == list:
            for j in range(len(int_list[i])):
                if int_list[i][j] > max_val:
                    max_val = int_list[i][j]
        else:
            if int_list[i] > max_val:
                max_val = int_list[i]
    return max_val


def reverse_rec(int_list):   # must use recursion
    """recursively reverses a list of numbers and returns the reversed list
    If list is None, raises ValueError"""
    pass


def bin_search(target, low, high, int_list):  # must use recursion
    """searches for target in int_list[low..high] and returns index if found
    If target is not found returns None. If list is None, raises ValueError """
    pass
