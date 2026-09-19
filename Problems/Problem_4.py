number = int(input("Enter a number : "))
out = True
if number == 1:
    print("Neither prime not composite")
elif number == 2:
    print("Prime")
elif number % 2 == 0:
    print("Not Prime")
else:
    n = number ** 0.5
    for i in range(2,int(n)+1):
        if number%i==0:
            print("Not prime")
            out =  False
    if out == True:
        print("Prime")