#  Count Even and Odd Numbers

a = list(map(int, input("Enter numbers: ").split()))

even = 0
odd = 0

for i in a:
    if i % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

print("Even:", even)
print("Odd:", odd)