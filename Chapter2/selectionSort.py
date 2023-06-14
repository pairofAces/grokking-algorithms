# create an initial function that will find the smallest element in an array

def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    # create a new array
    newArr = []

    # traverse the array
    for i in range(len(arr)):
        # invoke the findSmallest function to find the smallest element's index
        # and append that element into the new array
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))

    # return the new array
    return newArr