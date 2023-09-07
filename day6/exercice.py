
names = []
for i in range(4):
    a = input("Emter a name: ")
    names.append(a + "\n")
file = open(r"C:\Users\starinfo\Softy Education\day6\inputs.txt", 
"a")
file.writelines(names)
file.close()