names = ["Chahd", "Semi", "Mahmoud", "Jamel", "Mondher"]

del names[0]
del names[2]
del names[-1]

#del names[names.index("Mahmoud")]

names[names.index("Mahmoud")] = "Rami"
names.remove("Semi")
print(names)



