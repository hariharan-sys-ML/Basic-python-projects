number = int(input("Enter a number : \n"))
rev = 0
while number>0:
    n = number%10
    rev = rev * 10 + n
    number//=10
print(rev)