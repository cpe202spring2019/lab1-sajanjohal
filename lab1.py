# Sajan Johal
# Lab 1 Part 1


# max list iter pseudo code
# if the list is empty, return None
# if the list is None, raise ValueError
# set max_val really low (-1000000000000)
# use for loop to cycle through given list
# if the value at the index is another list, just a second for loop to cycle through that list
# if the value at that index(es) is greater than max, set max to that value
# return max

def max_list_iter(int_list):
    """finds the max of a list of numbers and returns the value (not the index)
    If int_list is empty, returns None. If list is Non, raises ValueError"""

    if int_list == []:
        return None
    elif int_list is None:
        raise ValueError

    max_val = -1000000000000
    for i in range(len(int_list)):
        if type(int_list[i]) == list:
            for j in range(len(int_list[i])):
                if int_list[i][j] > max_val:
                    max_val = int_list[i][j]
        elif type(int_list[i]) == int:
            if int_list[i] > max_val:
                max_val = int_list[i]
    return max_val


# reverse_rec pseudo code
# if the input list is empty, return a empty list
# return the last value of the index plus what the function call returns when given the list minus the last value

def reverse_rec(input_list):
    """recursively reverses a list of numbers and returns the reversed list
    If list is None, raises ValueError"""

    if not input_list:
        return []
    return [input_list[-1]] + reverse_rec(input_list[:-1])


# bin search pseudo code
# if the lower index is not higher than the higher index, raise ValueError
# find the middle index of the list
# if the value at the middle index is less than target, return bin search call but from mid + 1 and high
# if the value at the mid index is more than target, return bin search call but low and mid for parameters
# if the value at the mid index is equal to target, return mid index

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