
def check_duplicates(list, item):
    duplicates = 0
    for i in list:
        if i == item:
            duplicates += 1
    print(duplicates)
list = [1, 1, 1, 5, 9, 6, 1]
item = int(input("Enter a number: "))
check_duplicates(list, item)
