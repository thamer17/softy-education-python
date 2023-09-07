def greeting():
    print("Hello Thamer")
    print("Hello Ahmed")
    print("Hello Sami")

greeting()
greeting()
greeting()

def my_pet(name, age):
    message = "My pet is a cat and the name is " + name + " and the age is " + age
    return message
my_message = my_pet("Mimi", "8")
my_message2 = my_pet("Pascal", "7")

print(my_message)
print(my_message2)

# calcule

def calculate(a, b):
    result = (a, " + ", b, " = ", a+b)
    return result
r = calculate(5, 6)
print(r)
