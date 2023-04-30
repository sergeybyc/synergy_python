# Задание №1
# Создайте класс Касса, который хранит текущее количество денег в кассе, у него есть методы:
# top_up(X) - пополнить на X
# count_1000() - выводит сколько целых тысяч осталось в кассе
# take_away(X) - забрать X из кассы, либо выкинуть ошибку, что не достаточно денег

class Kassa:
	def __init__(self, current_money):
		self.current_money = current_money

	def top_up(self, X):
		self.current_money = self.current_money + X
		return
	
	def count_1000():
		pass
	
	def take_away(self, X):
		if X > self.current_money:
			print('Недостаточно средств для снятия')
		else:
			self.current_money = self.current_money - X
		return

	def Terminal(self):
		print(f'\nДенег в кассе: {qiwi.current_money}')
		print('\nДля пополнения введите 1:')
		print('Для снятия введите 2:')
		print('Остановить терминал 3:')
		ask = int(input())
		if ask == 1:
			print('Введите сумму для пополнения:')
			summ = int(input())
			self.top_up(summ)
			self.Terminal()
		elif ask == 2:
			print('Введите сумму для снятия:')
			summ = int(input())
			self.take_away(summ)
			self.Terminal()
		elif ask == 3:
			print('Выход')
			return
		else:
			print('Ошибка ввода')
			self.Terminal()

print('Задание №1:')
qiwi = Kassa(0)
qiwi.Terminal()

# Задание №2
# Создайте класс Черепашка, который хранит позиции x и y черепашки, а также s - количество клеточек, на которое она перемещается за ход
# у этого класс есть методы:
# go_up() - увеличивает y на s
# go_down() - уменьшает y на s
# go_left() - уменьшает x на s
# go_right() - увеличивает y на s
# evolve() - увеличивает s на 1
# degrade() - уменьшает s на 1 или выкидывает ошибку, когда s может стать ≤ 0
# count_moves(x2, y2) - возвращает минимальное количество действий, за которое черепашка сможет добраться до x2 y2 от текущей позиции

print('\n\nЗадание №2')

import math
class Cherepashka:
	def __init__(self, x, y, s):
		self.x = x
		self.y = y
		self.s = s
		if self.s < 1:
			self.s = 1
	def go_up(self, s):
		self.x = self.x + s
		
	def go_down(self, s):
		self.x = self.x - s
		
	def go_left(self, s):
		self.y = self.y - s

	def go_right(self, s):
		self.y = self.y + s
		
	def evolve(self, s):
		self.s = self.s + 1
		
	def degrade(self, s):
		if self.s > 1:
			self.s = self.s - 1

		else:
			print('s < 1')

	def count_moves(self, x2, y2):
		"""
		Возвращает минимальное количество действий, за которое черепашка сможет добраться до x2 y2 от текущей позиции
		Давайте ограничим значения х2 и у2 в этой функции - х<=10, у<=10, либо при подсчете количества действий будем шаг считать неизменным.
		"""
		print(f'\nНужно переместиться на y = {x2}, y = {y2}')
		
		countX = math.ceil((x2 - self.x) / self.s)
		countY = math.ceil((y2 - self.y) / self.s)

		print(f'\nПодсчитываю действия...\nМинимальное количество действий с шагом {self.s}: {countX + countY}\n({countX} ходов по оси X и {countY} ходов по оси Y)')
		return

	def locate(self):
		print(f'\nТекущие координаты: x = {self.x} y = {self.y} Шаг = {self.s}')

def play(x, y, s):
	print('\nВыберите действие:\n1 - go_up\n2 - go_down\n3 - go_left\n4 - go_right\n5 - evolve(увеличить шаг на 1)\
		\n6 - degrade(уменьшить шаг на 1)\n7 - count_moves(подсчитать количество ходов до точки)')
	select = int(input())
	if select == 1:
		animal.go_up(s)
	elif select == 2:
		animal.go_down(s)
	elif select == 3:
		animal.go_left(s)
	elif select == 4:
		animal.go_right(s)
	elif select == 5:
		animal.evolve(s)
	elif select == 6:
		animal.degrade(s)
	elif select == 7:
		print('\nВыберите куда переместиться:\nВведите x:')
		x2 = int(input())
		print('Введите y:')
		y2 = int(input())
		animal.count_moves(x2,y2)
	else:
		print('Команда не распознана')
	animal.locate()
	play(x, y, s)

# Приветствие
print('\nДавайте укажем начальные координаты и размер шага черепашки\nВведите x:')
x = int(input())
print('Введите y: ')
y = int(input())
print('Введите s(размер шага): ')
s = int(input())

# Создание
animal = Cherepashka(x, y, s)
print(f'\nВы создали черепашку. Текущие координаты:\nx = {animal.x} y = {animal.y} Шаг = {animal.s}')

# Интерфейс
play(animal.x, animal.y, animal.s)