num = int(input("Enter the number you want the multiplication table for: "))

for i in range(1, 11):
    result = num * i
    print(i, "*", num, "=", result)