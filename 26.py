# Write a Python program to remove duplicate characters from a string without using set()

# Take a string as input
s = input("Enter a string: ")

# Initialize an empty string
result = ""

# Check each character
for i in s:
    # Add the character only if it is not already present
    if i not in result:
        result = result + i

# Print the result
print("String after removing duplicates:", result)


# Enter a string: prasanna
# String after removing duplicates: prasn