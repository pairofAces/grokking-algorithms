# create a binary search function that takes a sorted array and an integer, item.
# If the item is in the array, the function will return its position. 

def binarySearch(sortedarray, item):
    # create pointers to keep track of the index locations
    low = 0
    high = len(sortedarray) - 1

    # while the search hasn't been narrowed down to a single element
    while low <= high:
        # create a pointer to keep track of the middle index location
        mid = (low + high) // 2
        # create a variable to represent the element in the middle of the list
        guess = sortedarray[mid]
        # check to see if the element is equal to the item being searched for
        if guess == item:
            # if yes, return the index of the element
            return mid
        # if the guess was too high
        if guess > item:
            # change the high pointer to be 1 less than the current mid,
            # removing all the elements that are too high, reducing the amount of
            # elements the algorithm needs to check
            high = mid - 1
        # if the guess was too low
        else:
            # change the low pointer to be 1 more than the current mid,
            # removing all elements that are too low
            low = mid + 1
    # if the item isn't in the input array, return None
    return None


# test
list1 = [1,3,5,7,9]
list2 = []
for i in range (1, 100):
    list2.append(i)
print(binarySearch(list1, 3))
print(binarySearch(list2, 99))