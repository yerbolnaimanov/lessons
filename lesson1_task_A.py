import math
def getLength():
    length=-1
    try:
        radius = int(input("ВВЕДИТЕ РАДИУС: "))
        length=2*math.pi*radius
    except Exception as e:
        print(e)
    return round(length, 2)

print(getLength())