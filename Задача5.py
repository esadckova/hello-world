a = float(input("Сообщите значение выручки фирмы"))
b = float(input("Сообщите значение издежек фирмы"))
c = a - b
if c < 0:
    print("Вы получили убыток", c)
if c == 0:
    print("Вы не получили прибыли")

else:
    d = 100 * c / a
    print("Вы получили прибыль", c)
    print("Рентабельность выручки составила", " %.3f" " процентов" % (d))
    z = int(input("Сообщите количество сотрудников фирмы"))
    f = c / z
    print("Прибыль фирмы на одного сотрудника составила", " %.3f" % (f))
