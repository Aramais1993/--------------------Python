# Дан список чисел. Определите, сколько в нем 
# встречается различных чисел. 

# myList = [1, 1, 2, 0, -1, 3, 4, 4]
# print(len(set(myList)))
# print(set(myList))


# Дана последовательность из N целых чисел и число K. 
# Необходимо сдвинуть всю последовательность 
# (сдвиг - циклический) на K элементов вправо,  K – положительное число.

# myList = [1,2,3,6,7,-9,0]
# n = int(input("Введите сдвиг: ")) % len(myList)
#for i in range(n):
#    myList.insert(0,myList.pop())
# print(myList)


# Напишите программу для печати всех уникальных значений в словаре.

# myList = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, 
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]  

# result = []
# for item in myList :
#    result.append(list(item.values())[0])
# print(set(result))
