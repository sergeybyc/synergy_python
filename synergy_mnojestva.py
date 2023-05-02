# Задание №1
# В первую строку вводится число N – количество чисел (1 ≤ N ≤ 100000). Во вторую строку вводится через пробел N чисел, каждое не превышает 2*10e9 по модулю. 
# Требуется выяснить, сколько среди этих чисел различных. Выведите число, равное количеству различных чисел среди данных.

def check_unique(lst):
	print(f'\nВы ввели: {lst}\n')
	unique = []	
	for _ in set(lst):
		unique.append(_)
	print(f'Уникальных чисел: {len(unique)}')

def input_N():
	print('Введите число N при условии: 1 ≤ N ≤ 100000')
	N = int(input())
	if N < 1 or N > 100000:
		print('Число вне диапазона')
		input_N()
	else:
		print(f'N = {N}')
		print(f'\nВведите {N} чисел через пробел. Каждое число не должно превышать 100000')
		a = list(map(int, input().split()))
		
		errors = False
		
		if len(a) != N:	
			print(f'Ошибка! Введено не {N} чисел!\n')
			errors = True

		for _ in a:
			if _ > 100000:
				print(f'Ошибка! {_} превышает 100000\n')
				errors = True

		if errors == True:
			input_N()
		else:
			check_unique(a)
		
input_N()

# Задание №2
# Вводятся два списка чисел, которые могут содержать до 100000 чисел каждый. Все числа каждого списка находятся на отдельной строке. 
# Выведите, сколько чисел содержится одновременно как в первом списке, так и во втором.

import random

def compare_arrays(array_1, array_2):
	new_array = []
	for i in array_1:
		for j in array_2:
			if i == j:
				new_array.append(i)
				break
	print(f'Повторяющихся значений: {len(new_array)}')

def createArrays():
    array_1 = []
    array_2 = []
    x = int(input('Введите длину первого списка чисел: '))
    y = int(input('Введите длину второго списка чисел: '))
    print(f'Заполняем первый список из {x} чисел')
    for _ in range(x):
    	array_1.append(input('Введите число: '))
    print(f'Заполняем второй список из {y} чисел')
    for _ in range(y):
    	array_2.append(input('Введите число: '))
    compare_arrays(array_1, array_2)

print("\nЗадание №2")
createArrays()


# Задание №3
# Во входную строку водится последовательность чисел через пробел. Для каждого числа выведите слово ”YES” (в отдельной строке), 
# если это число ранее встречалось в последовательности или ”NO”, если не встречалось.

def check_unique(numbers):
	check_mn = set()
	for current_number in numbers:
		if current_number in check_mn:
			print(f'{current_number} - YES')
		else:			
			print(f'{current_number} - NO')
		check_mn.add(current_number)


def start():
	numbers = []
	print('Вводите числа через пробел:')
	numbers = list(map(int, input().split()))
	check_mn = set()
	check_unique(numbers)


print('\nПроверка на уникальность. YES - число встречалось, NO - число НЕ встречалось.')
start()