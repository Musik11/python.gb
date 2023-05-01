#Задача 1:

n = int(input("Введите количество монет : "))
count = 0
for i in range(n):
    v = int(input())
    if v == 1:
        count += 1
print(count if count<n/2 else n-count)
