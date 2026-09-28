# write a pythom code to search for an elementin the list of elements. If the element found then print previous and next value.else print as not found.


def function(a,element):
    for i in range(len(a)):
        if a[i] == element:
            return a[-1],a[+1]
    return -1
a = list(map(int, input('Enter n elements').split()))
element = int(input('Enter element to be found'))
result = function(a,element)
if result == -1:
    print('Element not found')
else:
    for x in result:
        print(x,sep = ' ')