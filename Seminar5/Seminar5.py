# import CustomFuncs
# print(CustomFuncs.LastFibo(7))

# Task 2:
# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. 
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные. 


# a = [1, 2, 3, 1, 2, 4, 5, 5]
# print(a)

# for item in a :
#    if item == max(a) :
#        item = min(a)
#    print(item)


# Task 3:
# Напишите функцию, которая принимает одно число и проверяет, 
# является ли оно простым Напоминание: Простое число - это число, которое имеет 2 делителя: 1  и n(само число)

# number = int(input("Введите число"))
# def is_simple(number) :
#    if number > 2 and number % 2 !=0 :
#        for i in range(3, number // 2) :
#            if number % i == 0 :
#                return False
#        return True
#    return False
# print(is_simple(number))

# Task 4:
# Дано натуральное число N и последовательность из N элементов. 
# Требуется вывести эту последовательность в обратном порядке.

# import CustomFuncs

# number = int(input("Input a number: "))
# CustomFuncs.reverse_range(number)
