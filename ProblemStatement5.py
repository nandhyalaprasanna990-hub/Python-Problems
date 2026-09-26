# write a python program to find max element in first half and min element  in second half.


a = [1,2,4,56,57,45,7,9,46,89]
n = len(a)
mid = n // 2
max_firsthalf = a[0]
min_secondhalf = a[mid]
for i in range(0,4):
    if a[i] > max_firsthalf:
        max_firsthalf = a[i]
for i in range(4,8):
    if a[i] < min_secondhalf:
        min_secondhalf = a[i]
print(f'max element in first half : {max_firsthalf} and min element in second half : {min_secondhalf}')