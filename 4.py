# Урок No6. Циклы while и for

# Задание №1

n = int(input("сколько чисел: "))
b = 0
for i in range(n):
    a = int(input("введи каждое число : "))
    if a == 0:
        b += 1
print("Колличество чисел равных нулю: ", b)



# Задание #2


x = int(input("натуральное число: "))
y = 0

for i in range(1, x + 1):
    if (x % i == 0) and (x <= 2e9):
        y += 1
       # print(i)
print("Колличество натуральных делителей: ", y)




# Задание #3


a = int(input("первое число: "))
b = int(input("второе число: "))
a <= b
c = []
for i in range(a, b +1):
    if i % 2 == 0:
        c.append(i)
print(" ".join(map(str, c)))


a = int(input("Первое число: "))
b = int(input("Второе число: "))
a >= b
c = []
for i in range(a, b + 1):
    if i % 2 == 0:
        c.append(i)
print(*c, sep=" ")


