def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
loop1 = True
while loop1:
    n1 = int(input("Enter the first number: "))
    loop = True
    while loop:
        print("SELECT A OPERATION ")
        for operation in operations:
            print(operation)
        op = input("Enter your choice :")
        n2 = int(input("Enter the second number: "))
        if op == "+":
            result = add(n1,n2)
        elif op == "-":
            result = subtract(n1,n2)
        elif op == "*":
            result = multiply(n1,n2)
        else:
            result = divide(n1,n2)
        print(f"Result is {result}")
        continue1 = input("Enter 'y' to continue with the result and press 'n' to start a new one or to exit  :")
        if continue1 == "y":
            n1 = result
        elif continue1 == "n":
            u = input("start a new one ?? Type 'yes' or 'no'")
            if u == "yes":
                loop = False
            elif u == "no":
                loop = False
                loop1 = False



