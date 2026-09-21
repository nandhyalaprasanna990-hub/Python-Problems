# Write a python code to print the index of an element appears in the tuple.
# -> n should be given by user.
# -> If element not found , print as no element found
# -> Sample input:t=(10,20,30,20,60,90) and n = 20
# -> Sample output: element found at index 1




# Make sure list t is defined first
t = [10, 20, 30, 40, 50]

n = int(input('Enter the int value: '))

for i in range(len(t)):
    if n == t[i]:
        print(f'{n} found at index {i}')
        break
else:
    # This aligns with the 'for' loop, executing only if no break occurred
    print('element not found')
