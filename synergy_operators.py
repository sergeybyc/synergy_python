# Задание №1
# Пользователь вводит целое число. Выведите его строку-описание вида "отрицательное четное число", "нулевое число", 
# "положительное нечетное число", например, численным описанием числа 190 является строка "положительное четное число". 
# Если число не является четным - выведите сообщение "число не является четным"

while True:
	try:
		a = int(input('Введите целое число '))
		if a > 0:
			result = ('Положительное')
			break
		elif a < 0:
			result = ('Отрицательное')
			break
		elif a == 0:
			result = ('Нулевое')
			break
	except ValueError:
		print('Вы ввели не число')

if a % 2 == 0 and a != 0:
	result += ' четное'
elif a % 2 != 0 and a != 0:
	result += ' не четное'
result += ' число'

print(result)

# Задание №2
# Дано слово из маленьких латинских букв. Сколько там согласных и гласных букв? Гласными называют буквы «a», «e», «i», «o», «u».
# Для решения задачи создайте переменную и в неё положите слово с помощью input()
# А также определите количество каждой из этих гласных букв Если какой-то из перечисленных букв нет - Выведите False


word = input(str('Введите слово из латинских букв '))
word_lst = []
for _ in range(len(word)):
	word_lst.append(word[_])
print(f'Вы ввели: {word_lst}')

lst = ['a', 'e', 'i', 'o', 'u']
print(f'Ищем: {lst}')

glasnie = []

# from itertools import zip_longest
# for i, j in zip_longest(word_lst, lst):
# 	if i == j:
# 		glasnie.append(i)

for i in word_lst:
	for j in lst:
		if i == j:
			glasnie.append(i)

print(f'Совпадение: {glasnie}')

print(f'Гласных: {len(glasnie)}')
print(f'Согласных: {len(word_lst)-len(glasnie)}')
