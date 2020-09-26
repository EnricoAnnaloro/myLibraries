"""
Binary search is a iterative algorithm that is used to efficiently locate
a target value within sorted sequence of n elements
"""

def binary_search_iterative(data, target, low, high):
    """Return True if target is found within indicated portion of Python list

    The search only considers the portion of data from data[low] to data[high]
    """
    while high >= low:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return False
    
if __name__ == "__main__":
    data = [4, 5, 7, 9, 10, 20, 100, 35, 67, 89, 90, 22]
    test1_solution = True
    test2_solution = False
    test3_solution = False
    test_1 = binary_search_iterative(data, 5, 0, len(data)-1)
    test_2 = binary_search_iterative(data, 44, 0, len(data)-1)
    test_3 = binary_search_iterative(data, 10, 5, len(data)-1)



    if test_1 != test1_solution:
        raise Exception(f'Test 1 was not passed! test_1 is {test_1}, should be {test1_solution}.')
    elif test_2 != test2_solution:
        raise Exception(f'Test 2 was not passed! test_2 is {test_2}, should be {test2_solution}.')
    elif test_3 != test3_solution:
        raise Exception(f'Test 3 was not passed! test_3 is {test_3}, should be {test3_solution}.')
    else:
        print("Tests passed.")