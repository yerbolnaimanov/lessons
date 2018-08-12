import math
def getLength():
    length=-1
    try:
        type = input("ВВЕДИТЕ БУКВУ R или D:")
        if type=="R":
            radius = int(input("ВВЕДИТЕ РАДИУС: "))
            length=2*math.pi*radius
        elif type=="D":
            diam = int(input("ВВЕДИТЕ ДИАМЕТР: "))
            length = math.pi * diam
    except Exception as e:
        print(e)
    return round(length, 2)

print(getLength())