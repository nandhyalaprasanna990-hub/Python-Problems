# Find the First Non-Repeating Character
# Given a string, find the first character that appears only once in the string.


s = input("Enter a string: ")

for i in s:
    if s.count(i) == 1:
        print(i)
        break