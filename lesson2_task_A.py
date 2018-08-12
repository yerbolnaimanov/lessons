# урок 2, задание А
#subtask1
fio = input("Как Вас зовут? ")
fio=fio.strip(' !,./?!@#$%^&*()_+=~\"')
print("Здравствуйте {0}, как ваше настроение?".format(fio))

#subtask2
number = 0
try:
    number = float(input("Введите число: "))
except:
    print("ошибка")

print("В процентах: "+'{:.2%}'.format(number))
print("В валюте: "+ '{:.2f}'.format(number)+"$")