# Welcome to Basic Calculator program

# user is required to enter three inputs, two numbers and an operator
num1 = input("please enter a number ")
operator = input("please enter an operator ")
num2 = input("please enter another number ")

# program calculates an answer based on user inputs
if operator == '+':
 result = float(num1)+float(num2)
elif operator == '-':
 result = float(num1)- float(num2)
elif operator == '*':
 result = float(num1)*float(num2)
elif operator == '/':
 result = float(num1)/float(num2)
else: result = print("error unable to calculate ")

print(result)