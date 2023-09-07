result = 1
N = int(input("Enter a number: "))

# using for loop
for i in range(1, N+1):
    result = result * i
print(result)

# using while loop
result = 1
counter = 1
while counter <= N:
    result = result * counter
    counter += 1
print(result)

# using recursion
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)
result = factorial(N)
print(result)