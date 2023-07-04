'''
Given an array(list) of numbers:
 [1, 3, 5, 17, 38, 43, 71]
Target = 38

We want to develop an algorithm that performs a binary search on the array(list) to get the index of the target provided (38)
Expected output in this case = 5

Pseudocode for the binary search function:
Start
    binary_search(list, target):
    repeat:
        low = 0
        high = len(list)-1 -> [Number of elements in the list-1] to get the highest index
        mid = (high+low)//2 -> Floor division
        if list[mid] == target:
            return mid
        else if list[mid] < target:
            low = mid + 1
        else
            high = mid - 1
    until low > high
Stop
'''
# Problem data:
numbers = [1, 3, 5, 17, 38, 43, 71]
target = 38


# Solution to the problem:

# Creating the binary_search function in python
def binary_search(numbers , target):
    low = 0
    high = len(numbers)-1    

    while (high >= low):
        mid = (high+low)//2
        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

# Recursive version of the above function
def rec_binary_search(numbers, target, low, high):
    if low > high:
        return False
    else:
        mid = (high+low)//2
        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            return rec_binary_search(numbers, target, mid+1, high)
        else:
            return rec_binary_search(numbers, target, low, mid-1)


# Calling the function with the given data
result = binary_search(numbers, target)
result_rec = rec_binary_search(numbers, target, 0, len(numbers)-1)
print(f'The number {target} is in index: {result}') # Prints '4'
print(f'(Recursive function) The number {target} is in index: {result}')
