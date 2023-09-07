l = [1, 10, 5, 20, 15]
# def sorting_list(l):
#     for i in range(len(l)):
#         i_1 = 0
#         i_2 = 1
#         while i_2 < len(l):
#             if l[i_1] > l[i_2]:
#                 temp = l[i_2]
#                 l[i_2] = l[i_1]
#                 l[i_1] = temp
#             i_1 += 1
#             i_2 += 1
#     return l
# print(sorting_list(l))

# correction
def sort_numbers(list_of_numbers):
    n = len(list_of_numbers)
    for i in range(n):
        for j in range(n-1):
            if list_of_numbers[j] > list_of_numbers[j+1]:
                temp = list_of_numbers[j]
                list_of_numbers[j] = list_of_numbers[j+1]
                list_of_numbers[j+1] = temp
    return list_of_numbers
print("\n\nBefore sorting:\n", l)
l = sort_numbers(l)
print("\n\nAfter sorting:\n", l)

