names = {"Thamer", "Ahmed", "Mortadha"}

for index, name in enumerate(names):
    print(name, " has position of ", index)

for index, name in enumerate(sorted(names)):
    print(name, " has position of ", index)

for index, name in enumerate(sorted(names, reverse=True)):
    print(name, " has position of ", index)

numbers = {1, 5, 9}

print(len(names))
print(min(numbers))
print(max(numbers))
