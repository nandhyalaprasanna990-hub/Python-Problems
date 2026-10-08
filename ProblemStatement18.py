# Problem: Move All Zeros to the End
# Given a list of integers, move all 0s to the end of the list while maintaining the order of the other elements.


a = list(map(int, input("Enter numbers: ").split()))

result = []

zero = 0

for i in a:
    if i == 0:
        zero = zero + 1
    else:
        result.append(i)

for i in range(zero):
    result.append(0)

print(result)