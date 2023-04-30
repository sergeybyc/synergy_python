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

def createArrays(x, y):
    array_1 = []
    for i in range(x):
        array_1.append(random.randint(1,10))
    print(f"Массив 1:")
    for _ in array_1:
        print(_)
    array_2 = []
    for i in range(y):
        array_2.append(random.randint(1,10))
    print(f"Массив 2:")
    for _ in array_2:
        print(_)
    compare_arrays(array_1, array_2)

print("\nЗадание №2")
x = int(input('Введите длину первого списка '))
y = int(input('Введите длину второго списка '))
if x > 0 and x < 100000 and y > 0 and y < 100000:
	array1=(createArrays(x, y))
else:
	print('Число вне диапазона')


# Задание №3
# Во входную строку водится последовательность чисел через пробел. Для каждого числа выведите слово ”YES” (в отдельной строке), 
# если это число ранее встречалось в последовательности или ”NO”, если не встречалось.

class Numbers:
	def __init__(self, current_numbers, base_of_numbers, unique_numbers):
		self.current_numbers = current_numbers
		self.base_of_numbers = base_of_numbers
		self.unique_numbers = unique_numbers

	def check_unique(self, base_of_numbers, current_numbers):
		for _ in current_numbers:
			if _ in unique_numbers:
				print(f'{_} - YES')
		for _ in base_of_numbers:
			if _ not in unique_numbers:
				unique_numbers.append(_)
				print(f'{_} - NO')

		self.start()

	def write_lst(self, current_numbers):
		for _ in current_numbers:
			base_of_numbers.append(_)
		self.check_unique(base_of_numbers, current_numbers)

	def start(self):
		print('Вводите числа через пробел:')
		current_numbers = list(map(int, input().split()))
		self.write_lst(current_numbers)

current_numbers = []
base_of_numbers = []
unique_numbers = []
print('\nПроверка на уникальность. YES - число встречалось, NO - число НЕ встречалось.')
j = Numbers(current_numbers, base_of_numbers, unique_numbers)
j.start()











# class IllegalException(Exception):
#     pass

# def task_3(repeat=False):
# 	if repeat:
# 		print("Попробуйте еще раз:")

# 	try:
# 		m = int(input('Введите m (максимальная масса лодки) При условии 1 ≤ m ≤ 10e6\n'))

# 		if m < 1 or m > 1000000:
# 			print('Ошибка! Недопустимая масса лодки!')
# 			raise IllegalException
			
# 		else:		
# 			n = int(input('Введите n (количество рыбаков) при условии 1 ≤ n ≤ 100\n'))
# 			if n < 1 or n > 100:
# 				print('Ошибка! Недопустимое количество рыбаков!')
# 				raise IllegalException
			
# 			else:
# 				createArray_3(m, n)
	
# 	except IllegalException:
# 		task_3(True)