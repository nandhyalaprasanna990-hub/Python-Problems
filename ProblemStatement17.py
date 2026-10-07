# Problem: Find the Missing Number
# Given a list containing numbers from 1 to N, one number is missing. Find the missing number.




a = list(map(int, input("Enter numbers: ").split()))

n = len(a) + 1

total = n * (n + 1) // 2

actual = 0

for i in a:
    actual = actual + i

missing = total - actual

print("Missing number:", missing)