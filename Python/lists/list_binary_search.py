'''
Given an array(list) of numbers:
 [1, 3, 5, 17, 38, 43, 71]
Target = 38

We want to develop an algorithm that performs a binary search on the array(list) to get the index of the target provided (38)

Pseudo-code:
Start
    Initialize Numbers = [1, 3, 5, 17, 38, 43, 71]
    Target = 38
    Low = 0
    High = 6
    Index = 0
    If Numbers[Index] > Target
        index = index -1
    Else if Numbers[index] < Target
        index = index + 1
    Otherwise
        Display index
    End if
Stop
'''

numbers = [1, 3, 5, 17, 38, 43, 71]
target = 38
low = 0
high = 6
index = 0

for i in range(len(numbers)):
    if numbers[index] > target:
        index -=1
    elif numbers[index] < target:
        index += 1
    else:
        print(f'Number {target} is in index: {index}')
        

