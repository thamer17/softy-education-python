# 1- open file
names_files = open(
r"C:\Users\starinfo\Softy Education\day6\names.txt",
 "r"
)
# 2- read file content
# content = names_files.read()
lines = names_files.readlines()
# line = names_files.readline()
# # 3- manipulation
# print("Content:\n", content)
# print("Lines:\n", lines)
# print("Line:\n", line)
list = []
for line in lines:
    list.append(line.replace("\n", ""))
print(list)
# 4- close
names_files.close()

# comment: ctrl + k + c