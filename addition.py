num1 = input("please enter the first number: ")
num2 = input("please enter the second number: ")

if num1.isdigit() and num2.isdigit():
    result = int(num1) + int(num2)
    print(result)
else:
    print("invalid input")

