# Task 1 - When given a list, the program should return a list of all
# the elements below the original list’s arithmetical mean.
'''
def allBelow(list):
    # Making sure there are at least 2 different numbers in the list
    list_size = len(list)
    if list_size < 2:
        print("Invalid Input")
        return

    # Setting up the total for the entire list and the arithmetical mean
    total = 0
    avg = 0

    # Determines the total for the list
    for i in range(0, list_size):
        total = list[i] + total

    # Determines the arithmetical mean
    avg = total / list_size

    # Setting up final results small will start out as the same as list, but the numbers will be replaced
    # with the numbers that are below the arithmetical mean
    small = list
    j = 0
    less = 0

    for i in range(0, list_size):

        # If current element is smaller than the mean, then
        if list[i] < avg:
            small[j] = list[i]
            j = j + 1
            less = j

    max = less
    j = 0
    # Show the results
    print("Numbers less than the arithmetical mean: ")
    for j in range (0, less):
        print(small[j], end=' ')

# List to test out program
list = [10, 0, 31, 4, 58, 16]
allBelow(list)
'''

# Task 2 - When given a list of elements, find the two lowest elements.
'''
# Needed for the math.inf usage for the initial setup of some variables and as a check later in the code
# math.inf = Makes a floating-point positive infinity
import math

def twoBelow(list):
    # Making sure there are at least 2 different numbers in the list
    list_size = len(list)
    if list_size < 2:
        print("Invalid Input")
        return
    # Sets up the first and second numbers
    first = math.inf
    second = math.inf

    # Goes through list to find the lowest numbers
    for i in range(0, list_size):

        # If current element is smaller than first then, change current first number to second number
        # Then make current element the first number
        if list[i] < first:
            second = first
            first = list[i]

        # If current element is bigger than first, but smaller than second, then make it second
        elif list[i] < second and list[i] != first:
            second = list[i]

    # On the chance there are no other different numbers or there are only 2 numbers in list
    if second == math.inf:
        print("No second smallest element")

    # Show the results
    else:
        print("Smallest number:", first, "\nSecond smallest number:", second)


# List to test out program
list = [22, 93, 14, 20, 34, 50]
twoBelow(list)
'''
