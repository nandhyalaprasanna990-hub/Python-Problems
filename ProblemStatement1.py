# write a program to count how many times n appears in the tuple.

t = (10,20,30,10,40,60,90,10)
n =10
count = 0
for i in t:
    if i == n:
        count += 1
print(f'{n} appears {count} times')