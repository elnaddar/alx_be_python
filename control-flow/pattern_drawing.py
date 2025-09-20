i = size = int(input("Enter the size of the pattern: "))

while i > 0:
    j = size
    while j > 0:
        print("*", end="")
        j -= 1
    print()
    i -= 1