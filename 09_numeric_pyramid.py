# Assignment 9: Advanced Numeric Pattern Generator
# Print a number pyramid using nested loops.

n = int(input("Enter number of rows: "))

if n <= 0:
    print("Number of rows must be positive.")
else:
    for i in range(1, n + 1):
        for j in range(n - i):
            print(" ", end="")

        for j in range(1, i + 1):
            print(j, end=" ")

        print()
