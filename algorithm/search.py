def search(array, item):
    position = None
    for i in range(len(array)):
        if array[i] == item:
            position = i
    if position == None:
        print("Not found")
    else:
        print("Found at postion ", position)
list = [15, 17, 16, 20, 18, 19]
search(list, 18)


def search(array, item):
    for i in range(len(array)):
        if array[i] == item:
            return "Found at position " + str(i)
    return "Not found"
list = [15, 17, 16, 20, 18, 19]
result = search(list, 18)
print(result)

def search(array, item):
    position = None
    for i in range(len(array)):
        if array[i] == item:
            position = i
            break
    if position == None:
        print("Not found")
    else:
        print("Found at postion ", position)
list = [15, 17, 16, 20, 18, 19]
search(list, 18)