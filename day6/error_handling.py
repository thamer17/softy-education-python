names = ["Ahmed", "Chahd"]

#try:
#    print(names[2])
#except IndexError:
#    print("There is no names[2]")
#    print(names[-1])

try:
    x = float(input("Enter x: "))
    y = float(input("Enter y: "))
    print(x/y)
except ZeroDivisionError:
    print("Can't divide by zero")
except ValueError:
    print("x and y should be numbers")
else: 
    print("It works only if there is no error")
finally: 
    print("Always works")