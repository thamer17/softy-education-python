names = {"Thamer", "Ahmed", "Mortadha"}
other_names = {"Kamel", "Semi"}
 
names.discard("Ahmed")
names.update({"Rabeb", "Jamel", "Radhia"})

print("Names before update: ", names)
names.update(other_names)
print("Names after update: ", names)