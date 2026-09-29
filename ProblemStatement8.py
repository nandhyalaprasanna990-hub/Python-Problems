def even_odd(a):
    even = []
    odd = []
    for i in a:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    print("Even:", *even)
    print("Odd:", *odd)
a = list(map(int, input("Enter values: ").split()))
even_odd(a)