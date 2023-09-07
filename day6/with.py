# # File is closed by with statment

# with open(r"C:\Users\starinfo\Softy Education\day6\names.txt", 
# "r") as names_file:
#     content = names_file.read()
#     print(content)

# # We need to close

# names_file = open(r"C:\Users\starinfo\Softy Education\day6\names.txt", 
# "r")
# content = names_file.read()
# print(content)
# names_file.close()
try:
    with open(r"C:\Users\starinfo\Softy Education\day6\names.txt", 
 "r") as names_file:
        content = names_file.read()
        print(content)


except FileNotFoundError:
    print("File doesn't exist!")
except SyntaxError:
    print("Make sure to use the 'r' for Windows!")