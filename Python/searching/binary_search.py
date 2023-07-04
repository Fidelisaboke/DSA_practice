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

# Recursive binary search
def binary_search(numbers, target, low, high):
    if low > high:
        return False
    else:
        mid = (high+low)//2
        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            return binary_search(numbers, target, mid+1, high)
        else:
            return binary_search(numbers, target, low, mid-1)
        
        
# Slightly different interpretation but works the same way anyway
def alt_binary_search(numbers, target, low, high):
    if low > high:
        return False
    else:
        mid = low + (high-low)//2 # is this the same as (high+low)//2
        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            return binary_search(numbers, target, mid+1, high)
        else:
            return binary_search(numbers, target, low, mid-1)
        
        
# Running the binary search program:
from time import sleep

numbers = []
target = 0

while True:
    print(f'''
          Binary search programme
          Select Option:
          1. Insert Data
          2. Find Element
          0. Exit
          
          Current List: {numbers}
          ''')
    
    option = input('>')
    if option == '1':
        try:
            number = int(input('Enter data element:'))
            numbers.append(number)
            sleep(1)
        except ValueError:
            print('Please enter an integer.')
            
    elif option == '2':
        try:
            target = int(input('Enter the number to search:'))
            sorted_nums = sorted(numbers)
            sleep(1)
            index = binary_search(sorted_nums, target, 0, len(numbers)-1)
            index_alt = alt_binary_search(sorted_nums, target, 0, len(numbers)-1)
            if(index or index_alt == False):
                print('Number not in the list')
            else:
                print(f'The number {target} is in index: {index}')
                print(f'The number {target} using the alt binary search is in index: {index_alt}')
        except ValueError:
            print('Please enter an integer.')
    elif option == '0':
        print('Exiting script...')
        sleep(1)
        break