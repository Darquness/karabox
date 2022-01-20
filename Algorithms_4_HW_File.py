# Task 1 - Python program to segregate even and odd elements of array
'''
def numsort(nums, length):
    # Setting up for the traversal and swapping of indexes
    # Left is for even and right is for odd
    left, right = 0, length - 1

    # Count of number of
    # odd numbers, used in
    # slicing the array later.
    j = 0


    while (left < right):

        # While right is odd, decrement right by 1
        while (nums[right] % 2 == 0 and left < right):
            right -= 1

        # While left is even, increment left and j by 1
        while (nums[left] % 2 != 0):
            left += 1
            j += 1

        # Swap the left and right
        if (left < right):
            nums[left], nums[right] = nums[right], nums[left]

    # Slice the array based on even being first, then odds
    even = nums[j:]
    odd = nums[:j]


    # Sort the odd and even array accordingly
    even.sort()
    odd.sort()


    # Extend the even array with odd to make it a complete array again
    even.extend(odd)

    return even


# Driving code and function call
length = 10
nums = [10, 33, 92,17, 5, 74, 25, 27, 56, 88]
segnum = numsort(nums, length)
for i in segnum:
    print(i, end=" ")
'''


# Task 2 - Python implementation for Adding one to number represented by digits
'''
# Needed for the operations
import math

def addOne(nums):
    length = len(nums)

    # Add 1 to last digit. Also determine if the second to last digit needs to incremented
    nums[length - 1] += 1
    carry = nums[length - 1] / 10
    nums[length - 1] = nums[length - 1] % 10

    # Traverse from the second last digit
    for i in range(length - 2, -1, -1):
        if (carry == 1):
            nums[i] += 1
            carry = nums[i] / 10
            nums[i] = nums[i] % 10

    # If carry is 1, we need to add, then increment 
    if (carry == 1):
        nums.insert(0, 1)


# driving code to function call
print("Please enter some numbers with a space between them.")
nums = [int(x) for x in input().split()]

addOne(nums)

for i in range(0, len(nums)):
    print(nums[i], end=" ")
'''