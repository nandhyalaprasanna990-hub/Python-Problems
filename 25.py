# Write a Python program to count how many times a particular character appears in a string.




# Take a string as input
s = input("Enter a string: ")

# Take the character to search
ch = input("Enter a character: ")

# Initialize count
count = 0

# Check each character in the string
for i in s:
    if i == ch:
        count += 1

# Print the character frequency
print("Frequency:", count)


# INPUT : 
# Enter a string: prasanna
# Enter a character: a


# OUTPUT : 

# Frequency: 3