'''
QuickSort is an efficient sorting algorithm. When implemented well it can be about
two or three times faster than its main competitors, MergeSort and HeapSort.

QuickSort is a divide and conquer algorithm. It works by selecting a 'pivot' element
from the array and partitioning the other elements into two sub-arrays, according 
to wheter they are less than or greater than the pivot. The sub-arrays are then 
sorted recursively.

QuickSort is a comparison sort, meaning that it can sort items of any type for which a
"less-than" relation is defined. Efficient implementation of QuickSort are not a stable 
sort, which means that the relative order of the equal sorted items is not preserved.

QuickSort works on average on O(n log(n)) for sorting n items, in the worst case it 
works on O(n^2).

Following there is a grafical representation of how each partitioning works:
UnsortedData = [7, 3, 6, 5, 9, 12, 15, 3, 6]
[3*, 7*, 6, 5, 9, 12, 15, 3, 6]
[3, 6*, 7*, 5, 9, 12, 15, 3, 6]
[3, 6, 5*, 7*, 9, 12, 15, 3, 6]
[3, 6, 5, 7, 9, 12, 15, 3, 6]
[3, 6, 5, 7, 9, 12, 15, 3, 6]
[3, 6, 5, 7, 9, 12, 15, 3, 6]
[3, 6, 5, 3*, 9, 12, 15, 7*, 6]
[3, 6, 5, 3, 6*, 12, 15, 7, 9*]
As we can see, the partitioning works as explained earlier.
'''


def partition(data, low, high):
    '''This function takes the last element as pivot, it first selects it as data[high],
    then it place it in the correct position, then places all smaller elements to the left of 
    pivot and the bigger elements to the right of pivot.

    Input:  data, should be an array/list of numbers
            low, starting index
            high, ending index

    Output: pivot_index, it is the index of the correctly placed pivot
    '''
    smaller_element_index = low-1
    pivot = data[high]

    for element_index in range(low, high):
        if data[element_index] <= pivot:
            smaller_element_index = smaller_element_index + 1
            data[smaller_element_index], data[element_index] = data[element_index], data[smaller_element_index]

    smaller_element_index = smaller_element_index + 1
    data[smaller_element_index], data[high] = data[high], data[smaller_element_index]
    return smaller_element_index


def quickSort(data, low, high):
    '''This function performs the quicksort algorithm over the data array

    Input:  data, should be an array/list of numbers
            low, starting index
            high, ending index

    Output: sorted array/list of data
    '''
    if high == 1:
        return data
    if low < high:
        pivot_index = partition(data, low, high)

        # Now recursively sort the two partitions
        quickSort(data, low, pivot_index-1)
        quickSort(data, pivot_index+1, high)
    
if __name__ == "__main__":
    testArray = [10, 7, 8, 9, 1, 5]
    sortedArray = [1, 5, 7, 8, 9, 10]
    quickSort(testArray, 0, len(testArray)-1)

    if testArray == sortedArray:
        print("Test passed")
    else:
        print("Test Failed")
