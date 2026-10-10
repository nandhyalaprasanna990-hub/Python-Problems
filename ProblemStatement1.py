# write a program to count how many times n appears in the tuple.

t = (10,20,30,10,40,60,90,10)
n =10
count = 0
for i in t:
    if i == n:
        count += 1
print(f'{n} appears {count} times')




## Explanation: Count How Many Times n Appears in a Tuple

# 1. First, create a tuple `t` containing the numbers 10, 20, 30, 10, 40, 60, 90, 10.

# 2. Assign `n = 10` because we want to count how many times 10 appears in the tuple.

# 3. Initialize `count = 0` to keep track of the number of occurrences.

# 4. Use a `for` loop to access each element in the tuple one by one.

# 5. Use the condition `if i == n` to check whether the current element is equal to 10.

# 6. If the condition is true, increment the count by 1 using `count += 1`.

# 7. Repeat this process until all the elements in the tuple have been checked.

# 8. Finally, use the `print()` statement to display the number and its total occurrences.

# Output:10 appears 3 times

