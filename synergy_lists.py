# Задание №1
# В первой строке вводится число N. Далее в N строк вводится N чисел (1 ≤ N ≤ 10000), по одному числу на строке. 
# Все числа по модулю не превышают 10e5. Переверните массив чисел. Выведите N чисел - перевернутый массив.

import random

def createArray(x):
    r = 0
    array = []
    for i in range(x):
        array.append(random.randint(1,10000))
        r += 1
    print(f"Массив:")
    for _ in array:
        print(_)
    print(f"Перевернутый массив:")
    array.reverse()
    for _ in array:
    	print(_)
    return array

print("Задание №1\nВведите N:")
x = int(input())
if x >= 1 and x <= 10000:
	array1=(createArray(x))
else:
	print('Число вне диапазона')

# Задание №2
# В первую строчку вводится число N (1 ≤ N ≤ 100 000). В следующую строку через пробел вводятся N чисел (1 ≤ Ai ≤ 10e9). 
# Вам требуется написать метод, который получает на вход массив и изменяет его таким образом, чтобы на первом месте стоял последний элемент, на втором - первый, на третьем - второй и т. д. 
# Выведите N чисел - измененный массив.

print("Задание №2\nВведите N:")
y = int(input())

def createArray_2(y):
	r = 0
	array = []
	for i in range(y):
		array.append(random.randint(1,100000))
		r += 1
	print(f"Массив:")
	for _ in array:
		print(_)

	lst = array
	shift = 1
	lst = lst[-shift:] + lst[:-shift]
	print('Сдвиг массива')
	for _ in lst:
		print(_)
	return array

if y >= 1 and y <= 100000:
	array1=(createArray_2(y))
else:
	print('Число вне диапазона')


# Задание №3
# На берегу реки стояли n рыбаков, все они хотели перебраться на другой берег. Одна лодка может выдержать не более m килограмм, при этом в лодку помещается не более 2 человек. 
# Определите, какое минимальное число лодок нужно, чтобы перевезти на другой берег всех рыбаков В первую строку вводится число m (1 ≤ m ≤ 10e6) - максимальная масса, которую может выдержать одна лодка. 
# Во вторую строку вводится число n (1 ≤ n ≤ 100) - количество рыбаков. В следующие N строк вводится по одному числу Ai (1 ≤ Ai ≤ m) - вес каждого путешественника. 
# Программа должна вывести одно число - минимальное количество лодок, необходимое для переправки всех рыбаков на противоположный берег.

class IllegalException(Exception):
    pass

def task_3(repeat=False):
	if repeat:
		print("Попробуйте еще раз:")

	try:
		m = int(input('Введите m (максимальная масса лодки) При условии 1 ≤ m ≤ 10e6\n'))

		if m < 1 or m > 1000000:
			print('Ошибка! Недопустимая масса лодки!')
			raise IllegalException
			
		else:		
			n = int(input('Введите n (количество рыбаков) при условии 1 ≤ n ≤ 100\n'))
			if n < 1 or n > 100:
				print('Ошибка! Недопустимое количество рыбаков!')
				raise IllegalException
			
			else:
				createArray_3(m, n)
	
	except IllegalException:
		task_3(True)

def createArray_3(m,n):
	r = 1
	a = []
	# Вес рыбаков
	for i in range(n):
		a.append(random.randint(1,m))
		
	print(f"\nГенерируем рыбаков весом 1 ≤ Ai ≤ {m}...\n\nРыбаки:")
	for _ in a:
		print(f'Рыбак № {r} - {_} кг')
		r += 1

	# Заносим пары в список
	b = []
 
	for x in range(len(a)):
	    if a[x] + min(a) <= m:
	        b += [[a[x], min(a)]]
	        a[x] += m
	        a[a.index(min(a))] += m
	        # print(a[x])
	    else:
	        if a[x] > m:
	            continue
	        else:
	            b += [[a[x]]]

	print(f'\nМинимальное количество лодок: {len(b)}')
	# print(b)

task_3()