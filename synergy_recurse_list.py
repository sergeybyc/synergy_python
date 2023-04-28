my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def recursePrint(lst):
	if lst:
		print(lst.pop(0))
		recursePrint(lst)
	else:
		print('Конец списка')

recursePrint(my_list)
