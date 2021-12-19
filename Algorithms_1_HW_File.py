#Task 1 - Compute the sum of digits in all numbers from 1 to n.
'''
#Function to calculate the sum of every integer from 1 to n
#Then, returns the sum as the result.
def numSum(n):
    sum = 0
    i = 1
    while i <= n:
        sum = sum + i
        i = i + 1

    return sum


#Allows the user to input an integer, then passes it to the numSum function
print("Enter an integer, then the sum of all digits between 1 and the integer you chose will be calculated.")
n = int(input("Enter an integer: "))

sum = numSum(n)

print("The sum of all of the digits is: ", + sum)
'''
#End Task 1


#Task 2 - Find max number from 3 values, entered manually from a keyboard.
'''
# Function comparing a, b, and c to determine the largest integer
def maxNum(a, b, c):
    max = 0
    if (a >= b) and (a >= c):
        max = a

    elif (b >= a) and (b >= c):
        max = b

    else:
        max = c

    return max

# Allows the user to enter an integer for a, b, and c. 
# Then it passesthose integers to the maxNum function.
print("Enter three integers, then the largest integer of the three will be displayed.")
a = int(input("Enter integer a: "))
b = int(input("Enter integer b: "))
c = int(input("Enter integer c: "))

max = maxNum(a, b, c)

print("The largest integer of the three is: ", + max)
'''
#End Task 2


#Task 3 - Count odd and even numbers. Count odd and even digits of the whole number.
'''
# Allows user to  chose an integer for the program to use.
print("Enter an integer. The number of odd and even numbers the comprised the whole integer used will be displayed.")
wholeNum = str(input("Enter an integer: "))

# Separates the individual numbers that make up the whole integer into an array or list. Ex: 2021 becomes [2, 0, 2, 1]
# This allows for each individual number to be analyzed. 
arrayNum = [int(n) for n in str(wholeNum)]

# setting up the odd and even tallies
odd = 0
even = 0

# goes through the individual numbers and determines if its odd or even
for wholeNum in arrayNum:

    if wholeNum % 2 == 0:
        even += 1

    else:
        odd += 1

# Displays the odd and even tally results
print("Odd numbers used in chosen integer: ", odd)
print("Even numbers used in chosen integer: ", even)
'''
#End Task 3