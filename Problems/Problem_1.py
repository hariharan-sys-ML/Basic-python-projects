number = int(input("Enter a number :\n"))
if number%2 == 0:
    print("The number is Even\n")
else:
    print("The number is odd\n")

if number >= 0 :
    print("The number is positive\n")
else :
    print("The number is negative\n")

if number % 3==0 and number%5==0:
    print("Both 3 and 5\n")
elif number% 3==0 and number%5!=0:
    print("Only 3")
elif number % 3!=0 and number%5==0:
    print("Only 5")
else:
    print("Not divisible by 3 and 5")