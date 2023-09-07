# 1- open file
names_files = open(
r"C:\Users\starinfo\Softy Education\day6\names.txt",
 "w"
) # override
# 2- read file content
names = ["Ahmed\n", "Kamel\n"]
names_files.writelines(names)
# 3- close
names_files.close()
