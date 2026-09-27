# Write a python code to search for an element from the given list of elements linear search.



def linear_search(a,element):
    for i in a:
        if i==element:
           return True
    return False
a = list(map(int,input('Enter n elements').split()))
element = int(input('Enter element to be found'))
temp = linear_search(a,element)
if temp == True:
    print('Element found')
else:
    print('Element not found')

         
# for improve performence we can also remove temp


def linear_search(a,element):
    for i in a:
        if i==element:
           return True
    return False
a = list(map(int,input('Enter n elements').split()))
element = int(input('Enter element to be found'))
if linear_search(a,element):
    print('Element found')
else:
    print('Element not found')

