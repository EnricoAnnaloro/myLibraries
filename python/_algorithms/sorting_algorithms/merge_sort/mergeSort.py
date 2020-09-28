'''
Merge sort is an efficient, general-purpose, comparison-based sorting algorithm. Most implementation
will produce a stable sort although it not guaranteed, which means that the order of equal elements will remain the same as the
input. Merge sort is a divide and conquer algorithm.

Conceptually the algorithm works as follow:
    1 - Divide the unsorted list into n sublists, each containing one element
    2 - Repeatedly merge sublists to produce new sorted sublists until there is only one sublist left.
        That one will be the sorted list

QuickSort works on average on O(n log(n)) for sorting n items, in the worst case it 
works on O(n log(n)) and in best case on O(n).
'''

def mergeSort(data):
    '''This function checks on the data array passed if the order of the elements
    is correct, otherwise it divides the list into two sublists and calls itself 
    recursively. If the two sublist are ordered, then it merge them into a single
    ordered list

    Input:  data = list to be sorted
    '''
    if len(data) > 1:
        middle_index = len(data)//2
        left_list = data[:middle_index]
        right_list = data[middle_index:]
        mergeSort(left_list)
        mergeSort(right_list)

        # Ordering the sub-arrays element by element
        left_index = right_index = data_index = 0
        while left_index < len(left_list) and right_index < len(right_list):
            if left_list[left_index] < right_list[right_index]:
                data[data_index] = left_list[left_index]
                left_index += 1
            else:
                data[data_index] = right_list[right_index]
                right_index += 1
            data_index += 1

        # Checking for remaining elements
        while left_index < len(left_list):
            data[data_index] = left_list[left_index]
            left_index += 1
            data_index += 1

        while right_index < len(right_list):
            data[data_index] = right_list[right_index]
            right_index += 1
            data_index += 1

if __name__ == "__main__":
    testArray = [10, 8, 7, 9, 1, 5]
    sortedArray = [1, 5, 7, 8, 9, 10]
    mergeSort(testArray)

    if testArray == sortedArray:
        print("Test passed")
    else:
        print("Test Failed")
        print(f"Sorted array is {testArray}")
        print(f"Correct array is {sortedArray}")
