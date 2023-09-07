#external packages
from pyjokes import get_joke
from art import text2art
# internal packages
from calcul import add
from calcul import minus
from calcul import mult
from greeting import say_hi

# x = int(input("Enter x: "))
# y = int(input("Enter y: "))
# # result = add(x, y)
# # result = minus(x, y)
# result = mult(x, y)
# print(f"{x} x {y} = {result}")

# say_hi("Thamer")
# joke = get_joke()
# print(joke)
name = text2art("Thamer")
print(name)
