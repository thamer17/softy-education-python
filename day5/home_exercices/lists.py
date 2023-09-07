# lists
# ex_1
list_of_integers = [1, 1, 3, 3, 5, 5, 9, 944, 944, 2, 2, 7, 8]
for integer in list_of_integers:
    if list_of_integers.count(integer) > 1:
        for i in range(list_of_integers.count(integer) - 1):
            list_of_integers.remove(integer)
print(list_of_integers)