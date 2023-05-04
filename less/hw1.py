#Задача 1:

n = int(input("Количество элементов в массиве : "))
a = []
for i in range(n):
    a.append(int(input()))
x = int(input("Число которое вы ищите : "))
count = 0
for i in a:
    if i == x:
        count += 1
print("Количество чисел которое вы искали : ", count)