# Given an array of integers, count how many numbers in the array are even.

# A number is considered even if it is completely divisible by 2, i.e., number % 2 == 0.

# Input
# The first line contains an integer N, representing the number of elements in the array.
# The second line contains N integers.
# Output
# Print the total number of even numbers present in the array.
# Example

# Input:

# 6
# 1 2 4 7 8 9

# Output: 3 







N = int(input('Enter values:'))
A = list(map(int, input().split()))

count = 0

for num in A:
    if num % 2 == 0:
        count += 1

print(count)