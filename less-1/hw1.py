#Задача 1: Найдите сумму цифр трехзначного числа.
#*Пример:*
#123 -> 6 (1 + 2 + 3)
#100 -> 1 (1 + 0 + 0) |
#-----------------------------------------------------
n = input("Введите трехзначное число: ")
n = int(n)

n1 = n % 10
n2 = n % 100 // 10
n3 = n // 100
 
print('Сумма цифр числа:', n1 + n2 + n3)