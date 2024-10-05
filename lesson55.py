# Приклади:
# [12, 3, 4, 10] => [10, 12, 3, 4]
# [1] => [1]
# [] => []
# [12, 3, 4, 10, 8] => [8, 12, 3, 4, 10]
num1 = [12, 3, 4, 10]

if len(num1) >= 1: #На случай, если чисел выходит больше чем 1, будет выполнятся последовательная функция
    last_number = num1.pop() #Создает переменную с удаленным последним числом
    num1.insert(0, last_number) #Меняет местами числа
print(num1)

num2 = [1]

if len(num2) >= 1:
    last_number = num2.pop()
    num2.insert(0, last_number)
print(num2)

num3 = []

if len(num3) >= 1:
    last_number = num3.pop()
    num3.insert(0, last_number)
print(num3)

num4 = [12, 3, 4, 10, 8]

if len(num4) >= 1:
    last_number = num4.pop()
    num4.insert(0, last_number)
print(num4)




