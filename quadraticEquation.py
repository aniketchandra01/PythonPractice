def roots(a,b,c):
    x = (-b - ((b**2 - (4 * a * c)))**1/2)/2 * a
    z = (-b + ((b**2 - (4 * a * c)))**1/2) * a
    print(f"{x} and {z} are the roots for the quadratic Equation : {a}x\u00b2 + {b}x + {c} = 0")

print("Give the value of a,b,c for the quadratic equation : ax\u00b2 + bx + c = 0")
a = int(input("Give the value for a : "))
b = int(input("Give the value for b : "))
c = int(input("Give the value for c : "))
roots(a,b,c)