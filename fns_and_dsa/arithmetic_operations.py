def perform_operation(num1,num2,operation):
    if operation == "+":
      return num1+num2
    elif operation == "-":
        return num1-num2
    elif operation == "*":
        return num1*num2
    elif operation == "/":
        if num2 == 0:
            return "Error: Division by Zero."
        return num1/num2
    else:
        return "Error, invalid operation."


            