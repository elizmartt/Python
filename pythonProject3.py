expression = input("Please input the expression: ")

parts = expression.split()

if len(parts) != 3:
    print("Error: Please input the expression in the format 'number operator number'.")
else:
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
        else:
            print("Error: Division by zero.")
    else:
        print("Error: Unsupported operator.")
