# Problem: First Non-Repeating Character


                                    
s = input("Enter a string: ")             # Take a string as input
found = False                    # Initially, no non-repeating character is found
for i in s:            # Check each character in the string
    if s.count(i) == 1:     # Check whether the character appears only once
        print(i)            # Print the first non-repeating character
        found = True        # Mark that a character has been found
        break
if not found:                # If no non-repeating character is found
    print("No non-repeating character")

## Explanation

# 1. input() : takes a string from the user.
# 2. found = False indicates that no non-repeating character has been found yet.
# 3. The for loop checks each character one by one.
# 4. s.count(i) counts how many times a character appears.
# 5. If the count is 1, the character is printed.
# 6. found = True indicates that a non-repeating character has been found.
# 7. break stops the loop after finding the first non-repeating character.
# 8. if not found prints a message if no such character exists.

## Example 1

# Input:aabbcde
# Output:c


## Example 2

# Input:aabbbccc


# Output:No non-repeating character

