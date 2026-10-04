# Finding second largest element

a = list(map(int, input("Enter numbers: ").split()))

largest = a[0]
second = a[0]

for i in a:
    if i > largest:
        second = largest
        largest = i
    elif i > second and i != largest:
        second = i

print("Second largest:", second)