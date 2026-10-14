# Write a Python program to count the number of words in a given string.



s = input("Enter a string: ")
words = s.split()
count = len(words)
print("Number of words:", count)



# Input : Python is a Programming language.
# Output : 5



# Explanation :
# 1. Take a sentence as input from the user.
# 2. Use `split()` to separate the sentence into individual words.
# 3. Use `len()` to count the words in the resulting list.
# 4. Store the count in the variable `count`.
# 5. Print the total number of words.



