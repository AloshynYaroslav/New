a = int(input("Введите стартовое число: "))
b = int(input("Введите число которое мы должны превысить: "))
while a < b:
    import time

    print("Значение числа ", a, " пока меньше ", b, ", попробуем добавить единицу...")
    time.sleep(1)
    a += 1
    if a == b:
        print("Ещё чуть чуть...")
        time.sleep(3)
        a += 1
        print("УРА! Финальный счёт: ", a, ":", b, " в нашу пользу!")
if a > b:
    print("Значение ", a, " больше ", b, ", поздравляем!")