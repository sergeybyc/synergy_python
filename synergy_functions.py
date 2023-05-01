print('Задание №1')
import math
q = int(input('Введите целое число: '))
fact_q = math.factorial(q)
print(f'Факториал числа {q}: {fact_q}\nСписок:')
for _ in range(fact_q, 0, -1):
  print(f'{math.factorial(_)}')

print('Задание №2')
def read(pets):
  # print(f'Текущая база:\n{pets}')
  if len(pets.keys()) > 0:
    print(f'\nВсего записей: {len(pets.keys())}\n')
    find_id = int(input(f'Введите id для поиска (от 1 до {len(pets.keys())}): '))
    # print(pets[find_id])
    # result = pets[find_id].items()
    for p_id, p_info in pets[find_id].items():
      # print("\nPerson ID:", p_id)
      find_name = p_id
    print(f"\nРезультат поиска:\nЭто {pets[find_id][find_name]['Вид питомца']} по кличке {find_name}. Возраст питомца: {pets[find_id][find_name]['Возраст питомца']}. Имя владельца {pets[find_id][find_name]['Имя владельца']}")
      # for key in p_info:
      #   print(key + ':', p_info[key])
      # print(f"Это {pets['Вид питомца']} по кличке {pets[0]}.\n Возраст питомца: {pets['Возраст питомца']}. Имя владельца: {pets['Имя владельца']}")
    dict_id = 1
  else:
    print('Нет записей!')

  welcome(dict_id, pets)

def delete(pets):
  id_to_delete = int(input(f'Введите id для удаления (от 1 до {len(pets.keys())}): '))
  try:
    del pets[id_to_delete]
    print(f'Удаляем запись...')
  except:
    print('\nНе удалось удалить или введен не существующий id!')
  dict_id = 1
  welcome(dict_id, pets)

def update(pets):
  update = True
  id_to_update = int(input(f'Введите id для редактирования (от 1 до {len(pets.keys())}): '))
  add_pet(id_to_update, pets, update)

def add_pet(dict_id, pets, update=False):
  
  while True:
    kind_of_animal = str(input('Кто ваш питомец? '))
    if not kind_of_animal.isalpha():
      print("\nИспользуйте только буквы!\n")
      continue

    elif kind_of_animal.isalpha():
      break

  while True:
    try:
      pet_age = int(input('Сколько лет питомцу? '))
      break

    except:
      print('\nОшибка ввода! Укажите возраст цифрами!\n')
      continue
  
  while True:
    pet_name = str(input('Как зовут питомца? '))
    if not pet_name.isalpha():
      print("\nУкажите кличку буквами!\n")
      continue
    elif pet_name.isalpha():
      break
  while True:
    pet_owner = str(input('Как зовут хозяина? '))
    if not kind_of_animal.isalpha():
      print("\nИспользуйте только буквы!\n")
      continue

    elif kind_of_animal.isalpha():
      break

  # pets = {pet_name: {'Вид питомца': kind_of_animal, 'Возраст питомца': pet_age, 'Имя владельца': pet_owner}}

  pets[dict_id] = {pet_name: {'Вид питомца': kind_of_animal, 'Возраст питомца': pet_age, 'Имя владельца': pet_owner}}
  if update == False:
    dict_id += 1
  welcome(dict_id, pets)
  # return pets, pet_name

def welcome(dict_id, pets):
  try:
    print(f'\nВсего записей: {len(pets.keys())}')
    print(f'\nТекущие записи:\n{pets}')
    select = int(input('\nВыберите действие:\n1 - Добавить нового питомца\n2 - Вывести информацию о питомце\n3 - Удалить запись\n4 - Редактировать запись\n0 - Выход\n'))
    if select == 1:
      add_pet(dict_id, pets)
    elif select == 2:
      read(pets)
    elif select == 3:
      delete(pets)
    elif select ==4:
      update(pets)
    elif select == 0:
      print('Выход')
    else:
      print('\nКоманда не распознана!\n')
      welcome(dict_id, pets)
  except:
    print('\nКоманда не распознана!\n')
    welcome(dict_id, pets)
    
    

# pets, pet_name = add_pet()
# print(f"Это {pets[pet_name]['Вид питомца']} по кличке {pet_name}. Возраст питомца: {pets[pet_name]['Возраст питомца']}. Имя владельца: {pets[pet_name]['Имя владельца']}")

pets = {}
welcome(1, pets)