pets = ["Cat", "Dog", "Hamster", "Bird", "Fish", "Turtle", "Cow"]
print("We have ", pets.count("Cat"), " cats.")
print("\n\npets with reverse:\n")
pets.reverse()#print(pets)

print("\n\npets with sorted reverse:\n")
print(sorted(pets, reverse=True))
pets.pop(0)
pets.pop()
pets.clear()
print(pets)