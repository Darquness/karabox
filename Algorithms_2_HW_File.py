# Task 1 - Given a string. Split it into two equal parts and show the results in reverse.
'''
# Allows user to  enter a string for the program to use.
print("Enter some characters. The program will slice it in half.")
chars = input("Enter some characters: ")

# reverse the string of characters
reverse = chars[::-1]

# Gets the total number of chars used and determines what half is
charSize = len(chars)
charHalf = charSize / 2

# Sets up the first and second half of the entire string
aHalf = int(charHalf)
bHalf = int(charHalf)

# Sets up the situation of the string not being even
# If it not even, then it will add the extra character to the first half
if charSize % 2 != 0:
    aHalf = int(charHalf) + 1

# takes the entire string and separates it into the first and second halves.
n = [aHalf, bHalf]
print(''.join([reverse[sum(n[:i]):sum(n[:i+1])] for i in range(len(n))]))
'''

# Task 2 - Determine if a string consists of all unique characters. If it does, then print True or else print False
'''
# Setting the maximum size of the array
arraySize = 256

def totalString(string):
    totalChars = [0] * arraySize
    for i in string:
        totalChars[ord(i)] += 1

    return totalChars

# Finds whether there are repeating characters or not in the string
def stringTraversal(string):
    totalChars = totalString(string)
    index = -1
    k = 0

    for i in string:
        if totalChars[ord(i)] != 1:
            index = k
            break
        k += 1

    return index

# Code that uses previous functions for string traversal to confirm
# the first unique character or none at all from user input
string = str(input("Enter string: "))

# "total" is number of characters from string + 1.
# This is to match the -1 value of index from the stringTraversal function if there are no unique characters
total = len(string) - (len(string) + 1)
index = stringTraversal(string)
if index == total:
    print("True")

else:
    print("False")
'''