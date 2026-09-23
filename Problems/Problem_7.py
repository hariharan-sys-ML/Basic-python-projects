User = input("Enter the sentence : ").lower()
lis = User.split()
largest = len(lis[0])
for i in lis:
    n = len(i)
    if n >= largest:
        large = i
        largest = n
print(f"The Largest word is '{large}' with {largest} number of letters")

