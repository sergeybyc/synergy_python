# Задание №1
# На вход подается 1 строка без пробелов. 
# По данной строке определите, является ли она палиндромом 
# (то есть, можно ли прочесть ее наоборот, как, например, слово "шалаш"). 
# Необходимо вывести ”yes”, если строка является палиндромом, и “no” в противном случае.

print('Введите строку без пробелов:')
line = input()

if int(len(line) % 2) != 0:
	count = int(len(line) / 2)
	first_part = line[0:count]
	second_part = line[count+1:len(line)][::-1]
	# print(first_part)
	# print(second_part)
	if first_part == second_part:
		print('yes')
	else:
		print('no')
else:
	count = int(len(line) / 2)
	first_part = line[0:count]
	second_part = line[count:len(line)][::-1]
	# print(first_part)
	# print(second_part)
	if first_part == second_part:
		print('yes')
	else:
		print('no')


# Задание №2
# Дана строка, длина которой не превосходит 1000. Вам требуется преобразовать все идущие подряд пробелы в один. Выведите измененную строку.

print('Введите строку не длиннее 1000 символов:')
line_1 = input()
if len(line_1) < 1000:
	line_1 = " ".join(line_1.split())
	print(line_1)
