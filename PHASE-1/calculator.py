operand1=int(input("Enter the operand1:"))
operand2=int(input("Enter the operand2:"))
operator=input("Enter the operator(+,-,*,/):")

def calculator(operand1,operand2,operator):
    if operator=="+":
        return (operand1+operand2)
    elif operator=="-":
        return (operand1-operand2)
    elif operator=="*":
        return (operand1*operand2)
    elif operator=="/":
        return (operand1/operand2)
    else:
        return "Invalid input, Please enter a valid arithematic operator"
    
print(calculator(operand1,operand2,operator))