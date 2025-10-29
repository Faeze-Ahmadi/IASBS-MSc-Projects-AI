length = int(input("Enter the length of rectangle: "))
width = int(input("Enter the width of rectangle: "))

area = length * width
perimeter = (length + width) * 2

request = input("Calculating area or perimeter? ")

if request == "area":
    print(area)
elif request == "perimeter":
    print(perimeter)
else:
    print("The only permitted request is 'area' or 'perimeter'.")