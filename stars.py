# for loop
x = int(input("Enter the height of the star: "))
for i in range(1, x+1):
    print("*"*i)

# Nested loop
y = int(input("Enter the height of the triangle (number of rows): "))
print("Right Triangle Pattern5")
for i in range(1, y + 1):
    for j in range(i):
        print("*", end="")
    print("")