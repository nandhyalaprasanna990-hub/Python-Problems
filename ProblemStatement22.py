# Write a Python program to count the number of vowels in a string.
# input : prasanna
# output : 3
# Take a string as input
s = input("Enter a string: ")

# Initialize vowel count to zero
count = 0

# Check each character in the string
for i in s:
    # Check whether the character is a vowel
    if i in "aeiouAEIOU":
        count += 1

# Print the total number of vowels
print("Number of vowels:", count)
