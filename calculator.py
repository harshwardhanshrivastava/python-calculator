num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
Op = input("Enter opernum1tor(+, -, *, /, %, **): ")

if Op == "+":
    print(num1 + num2)

elif Op == "-":
    print(num1 - num2)

elif Op == "*":
    print(num1 * num2)

elif Op == "/":
    print(num1 / num2)

elif Op == "%":
    print(num1 % num2)

elif Op == "**":
    print(num1 ** num2)

else:
    print("INVALID OPERATOR")

print("Thank You For Using a Python Calculator")