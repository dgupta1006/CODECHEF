l = int(input())
b = int(input())
area = int(l * b)
peri = int(2*(l+b))
if (area > peri):
    print("Area")
    print(area)
elif(peri==area):
    print("Eq")
    print(area)
else:
    print("Peri")
    print(peri)

