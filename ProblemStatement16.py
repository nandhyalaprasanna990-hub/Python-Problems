# Problem Statement:
# Given a list of integers and a target number, find how many times the target number occurs in the list.


a = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter target: "))

count = 0

for i in a:
    if i == target:
        count = count + 1

print("Target element not found")