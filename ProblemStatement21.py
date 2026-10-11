# Write a Python program to calculate the sum of all numbers in a tuple without using the built-in sum() function.


t = list(map(int, input('Enter the values: ').split()))

total = 0

for i in t:
    total = total + i

print("Sum of elements:", total)


# Explanation

# Take multiple values from the user

# Initialize total = 0 to store the sum of all elements.

# Use a for loop to access each element in the tuple one by one.

# The statement total = total + i adds the current element to the total.

# Repeat this process until all elements in the tuple have been added.

# Finally, use the print() statement to display the total sum.

# input : 1 2 3 4 5
# Output

# Sum of elements: 15