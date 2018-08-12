# елизовать формулу длины окружности через площадь круга
import math
def getLength():
    length=-1
    try:
        area = int(input("ВВЕДИТЕ ПЛОЩАДЬ: "))
        length=2*math.sqrt(area*math.pi)
    except Exception as e:
        print(e)
    return round(length, 2)

print(getLength())