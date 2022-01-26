# Task 1 - Selection Sort
'''
# Number selection by user
print("Please enter some numbers with a space between them.")
nums = [int(x) for x in input().split()]

# Array traversal
for i in range(len(nums)):

    # Find the minimum element and put it in to new list using "min"
    min = i
    for j in range(i + 1, len(nums)):
        if nums[min] > nums[j]:
            min = j

    # Swap the minimum element with the first element
    nums[i], nums[min] = nums[min], nums[i]

# Print results
for i in nums:
    print(i, end=" ")
'''

# Task 2 - Bubble Sort
'''
def bubbly(nums):
    length = len(nums)

    # Array traversal
    for i in range(length-1):

        for j in range(0, length-i-1):
            
            # Swap if element found is greater than the next element
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

# Number selection by user
print("Please enter some numbers with a space between them.")
nums = [int(x) for x in input().split()]

bubbly(nums)

for i in nums:
    print(i, end=" ")
'''

# Task 3 - Insertion Sort
'''
def insert(nums):

    # Traverse through 1 to len(arr)
    for i in range(1, len(nums)):

        min = nums[i]

        # Move elements greater than min to one position ahead of their current position
        j = i-1
        while j >=0 and min < nums[j] :
                nums[j+1] = nums[j]
                j -= 1
        nums[j+1] = min

# Number selection by user
print("Please enter some numbers with a space between them.")
nums = [int(x) for x in input().split()]

insert(nums)

for i in nums:
    print(i, end=" ")
'''

# Task 4 - Merge Sort
'''
# Array traversal
def merge(nums):
    if len(nums) > 1:
  
        # Determine half of array length
        mid = len(nums)//2

        #First half of array
        left = nums[:mid]

        # Second half of array
        right = nums[mid:]

        # Sorting the first half
        merge(left)

        # Sorting the second half
        merge(right)

        # Setting up for counters
        i = 0
		j = 0
		k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

# Number selection by user
print("Please enter some numbers with a space between them.")
nums = [int(x) for x in input().split()]

merge(nums)
for i in nums:
    print(i, end=" ")
'''