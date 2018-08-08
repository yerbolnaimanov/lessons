value=1
def getInput():
    '''
    метод получает значение через ст ввод
    :param text: текст инпута
    :defaultValue: значенеи возвращаемого инпутом по умолчанию
    :return: mixed
    '''
    try:
        value = input("ВВЕДИ ЧТО НИБУДЬ")
        return value
    except Exception as e:
        print("ошибка ввода")
        print(e)
        return False


x = getInput()
tries=3
i=0

while x==False:
    i+=1
    if i<tries:break
    x = getInput("Введите число: ")
    print(type(x))

print(value)