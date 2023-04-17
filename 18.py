# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# Пример:
# 5
#     1 2 3 4 5
#     6
#     -> 5
import random

n = int(input("Введите количество элементов в массиве: "))
array = []
for j in range(n):
    array.append(random.randint(0,10))
print(array)

minArr = array[0]
maxArr = 100

x = int(input("Введите X: "))
for i in range(len(array)):
    if (x == array[i]):
        result = x
        break
    elif (x > array[i]):
        if (x - array[i] < minArr):
            minArr = x - array[i]
    elif (x < array[i]):
        if (array[i] - x < maxArr):
            maxArr = array[i] - x
if (maxArr > minArr):
    result = x - minArr
else: result = x + maxArr 
print(f'-> {result}')