# create a file with "w" mode
with open(r"names2.txt", "w") as names_file:
    names = ["Rania\n", "Yassin\n", "Rawane"]
    names_file.writelines(names)
    print("names file created successfully!")
# read a file with "r" mode
with open(r"names2.txt", "r") as file_names:
    content= file_names.read()
    print(content)
# append name with with "a" mode
with open(r"names2.txt", "a") as file_name:
    file_name.write("\nMohamed")