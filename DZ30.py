# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и 
# количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: 
# an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

array = []
a1 = int(input('Input the first element a[0]: '))
d = int(input('Input the difference d: ')) # шаг
n = int(input('Input the elements quantity n: ')) # общее количество элементов
for i in range(1, n+1):
     array.append(a1 + (i-1)*d)
print(array)