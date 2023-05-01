#Задача 2:

x = int(input("Первое число : "))
y = int(input("Второе число : "))
for i in range(x):
    for j in range(y):
        if x == i + j and y == i * j:
            print(i, j)