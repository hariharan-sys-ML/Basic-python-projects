n = int(input("Enter a number : "))
a = 0
b = 1
for i in range(0,n):
    print(a)
    next_num = a + b
    a = b
    b = next_num