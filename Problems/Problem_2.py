number = int(input("Enter a Number : "))
lis = []
count = 0

while number > 0:
    n = number % 10
    lis.append(n)

    count += 1
    number //= 10

print(f"No.of Digits = {count}\n")

total = sum(lis)
print(f"The total sum of the digits is {total}\n")

temp = 0

for i in lis:
    if i > temp:
        temp = i
        largest = temp

print(f"The Largest digit is {largest}\n")

for i in lis:
    if i < temp:
        temp = i
        smallest = temp

print(f"The Smallest digit is {smallest}\n")