# Problem Statement:
# Given a list of integers, remove duplicate elements without using set().



a = list(map(int, input("Enter numbers: ").split()))

unique = []

for i in a:
    if i not in unique:
        unique.append(i)

print(unique)