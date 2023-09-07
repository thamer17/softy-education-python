# # using for loop
# def count_down(n):
#     while n >= 1:
#         print(n)
#         n -= 1
# n  = int(input("Enter number: "))
# count_down(n)

# using recursion 
def count_down(n):
    #base case
    if n == 0:
        return # exit function 
    print(n)
    count_down(n-1)
n  = int(input("Enter number: "))
count_down(n)
 