#Задача 2: Петя, Катя и Сережа делают из бумаги журавликов. 
#Вместе они сделали S журавликов. 
#Сколько журавликов сделал каждый ребенок, 
#если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
#а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
#*Пример:*
#6 -> 1  4  1
#24 -> 4  16  4
#60 -> 10  40  10

s = int(input('Сколько журавликов всего : '))
S = s / 6
P = S
E = (S + P) * 2
print(int(S), int(E), int(P))
