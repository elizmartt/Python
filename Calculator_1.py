expression = input("Please input the expression: ")

parts = expression.split()

x = parts[0]
operator = parts[1]
y = parts[2]
if operator == "+":
    result = int(x) + int(y)
    print(result)
elif operator == "-":
    result = int(x) - int(y)
    print(result)
elif operator == "*":
    result = int(x) * int(y)
    print(result)
elif operator == "/":
    if int(y) != 0:
        result = int(x) / int(y)
        print(result)

