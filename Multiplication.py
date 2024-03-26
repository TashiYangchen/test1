x = int(input("Enter the number for which you want the multiplication table:"))
y = int(input("Enter the limit up to which you want the multiplication table generated:"))
print("The multiplication table for: ", y)
for i in range (1, y + 1):
    print(f"{x} * {i} = {x*i}")