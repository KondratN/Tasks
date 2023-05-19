# 4.72 (а) Даны три различных вещественных числа. Не используя полный условный оператор, определить наибольший из них
# number1 = float(input('Введите первое число\n'))
# number2 = float(input('Введите второе число\n'))
# number3 = float(input('Введите третье число\n'))
# maximum = number1
# if number2 > maximum:
#     maximum = number2
# if number3 > maximum:
#     maximum = number3
# print(maximum)
# 4.72 б Даны три различных вещественных числа. Не используя полный условный оператор, определить наименьший из них
# number1 = float(input('Введите первое число\n'))
# number2 = float(input('Введите второе число\n'))
# number3 = float(input('Введите третье число\n'))
# minimum = number1
# if number2 < minimum:
#     minimum = number2
# if number3 < minimum:
#     minimum = number3
# print(minimum)
# 4.76 Составить программу, которая уменьшает первое введенное число в два раза, если оно больше второго введенного
# числа по абсолютной величине
# number1 = int(input('Введите первое число\n'))
# number2 = int(input('Введите второе число\n'))
# number3 = number1
# if number3 < 0:
#     number3 = number3 * (-1)
# if number3 > number2:
#     print('Первое число = ' + str(number3))
#     print('Второе число = ' + str(number2))
#     number3 = number3 / 2
#     print('Уменьшаем первое число на 2')
# else:
#     print('Первое число меньше второго числа по абсолютной величине')
# print('Первое число = ' + str(number3))
# print('Второе число = ' + str(number2))
# 4.78 Даны три целых числа. Вывести на экран те из них, которые являются четными
# number1 = int(input('Введите первое число\n'))
# number2 = int(input('Введите второе число\n'))
# number3 = int(input('Введите третье число\n'))
# if number1 % 2 == 0:
#     print(number1)
# if number2 % 2 == 0:
#     print(number2)
# if number3 % 2 == 0:
#     print(number3)
# 4.83 Даны четыре вещественных числа. Найти сумму тех чисел, которые больше пяти. Оператор цикла не использовать.
# number1 = float(input('Введите первое число\n'))
# number2 = float(input('Введите второе число\n'))
# number3 = float(input('Введите третье число\n'))
# number4 = float(input('Введите четвертое число\n'))
# sum = 0
# if number1 > 5:
#     sum = sum + number1
# if number2 > 5:
#     sum = sum + number2
# if number3 > 5:
#     sum = sum + number3
# if number4 > 5:
#     sum = sum + number4
# print(sum)
# 4.84 Даны четыре целых числа. Определить сумму тех из них, которые кратны трем. Оператор цикла не использовать.
# number1 = int(input('Введите первое число\n'))
# number2 = int(input('Введите второе число\n'))
# number3 = int(input('Введите третье число\n'))
# number4 = int(input('Введите четвертое число\n'))
# sum = 0
# if number1 % 3 == 0:
#     sum = sum + number1
# if number2 % 3 == 0:
#     sum = sum + number2
# if number3 % 3 == 0:
#     sum = sum + number3
# if number4 % 3 == 0:
#     sum = sum + number4
# print(sum)