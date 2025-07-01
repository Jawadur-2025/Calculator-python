# Get the input for the operation
operatino = input("Enter operation (+,-,*,/):")
# Get the input for the number
num1 = float(input("Enter first number :"))
num2 = float(input("Enter second number:"))
# perform the calculation base on the operation
if operatino =='+':
    result=num1+num2
elif operatino =='-':
    result=num1-num2
elif operatino =='*':
    result=num1*num2
elif operatino =='/':
    if num2 !=0:
        result=num1/num2
    else:
        result="Error! Devision by zero"
else:
        result="Invalid operation"

# Desplay the result 
print(f"Result : {result}")
