#Задача 2:

n = int(input("Количество элементов в массиве : "))
a = []
for i in range(n):
    a.append(int(input()))
x = int(input("Введите 'X' : "))
min_diff = abs(a[0] - x)
min_elem = a[0]
for i in range(1, n):
    diff = abs(a[i] - x)
    if diff < min_diff:
        min_diff = diff
        min_elem = a[i]
print("Число самый близкий по величине элемент к заданному числу 'X' : " , min_elem)