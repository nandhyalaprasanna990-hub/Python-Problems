# Problem: Find the Maximum Number in a Tuple

# Write a program to find the maximum number in a tuple.

t = (10, 25, 8, 40, 15, 30)

largest = t[0]

for i in t:
    if i > largest:
        largest = i

print("Maximum number:", largest)

# Code Explanation : 

# t = (10, 25, 8, 40, 15, 30)
# Creates a tuple containing six numbers.

# largest = t[0]
# Stores the first element, 10, in the variable largest. Initially, we assume it is the largest number.

# for i in t:
# Iterates through each element in the tuple one by one.

# if i > largest:
# Checks whether the current element is greater than the current largest value.

# largest = i
# If the condition is true, updates largest with the current element.

# print("Maximum number:", largest)
# Prints the largest number after checking all elements.