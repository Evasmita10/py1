print("---CALCULATOR---")
print("_Choose an option_")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Exponent")
print("6.Floor division")

choice=input("Enter choice (1/2/3/4/5/6): ")

a=float(input("Enter the first number: "))
b=float(input("Enter the second number: "))

if choice=="1":
    print("Result: ",a+b)

elif choice=="2":
    print("Result: ",a-b)

elif choice=="3":
    print("Result: ",a*b)

elif choice=="4":
    if b!=0:
        print("Result: ",a/b)
    else:
        print("Error! cannot Divide by zero: ")

elif choice=="5":
    print("Result: ",a**b)

elif choice=="6":
    print("Result: ",a//b)

else:
    print("Invalid choice")