a=input("Enter a value: ")
b=input("Enter b value: ")
c=input("Enter c value: ")
if a == b == c:
    print("Equilateral")
elif a == b or a == c or b == c:
    print("Isosceles")
else:
    print("Scalene")