a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

if a == b:
    if b == c:
        print("Equilateral")
    else:
        print("Isosceles")
else:
    if a == c:
        print("Isosceles")
    elif b == c:
        print("Isosceles")
    else:
        print("Scalene")
