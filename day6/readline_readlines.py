# readline --> get the first line 
with open(r"names2.txt", "r") as names_file:
    first_line = names_file.readline()
    print(first_line)
# readline --> get all lines in a list 
with open(r"names2.txt", "r") as names_file:
    all_lines = names_file.readlines()
    print(all_lines)
for position, line in enumerate(all_lines):
    print("Line ", position, " is: ", line)