import random

def ask(rows_or_columns):
    print(f"Введите количество {rows_or_columns}: ")
    number = int(input())
    return number

def createArray(x, y, num):
    r = 0
    array = []
    for i in range(x):
        array.append([])
        for j in range(y):
            array[i].append(random.randint(0,100))
            r += 1
    print(f"Матрица №{num}")
    for _ in array:
        print(_)
    return array

def emptyArray(x, y):
    r = 0
    empty_array = []
    for i in range(x):
        empty_array.append([])
        for j in range(y):
            empty_array[i].append(0)
            r += 1
    return empty_array

x=ask("строк")
y=ask("столбцов")
array1=(createArray(x,y,1))
array2=(createArray(x,y,2))
array3=(emptyArray(x,y))

def ArraySumm(A, B, C):
    for i in range(len(A)): 
        for j in range(len(A[0])): 
              C[i][j] = A[i][j] + B[i][j] 

    print("Сумма")
    for r in C:
        print(r) 
    return C

ArraySumm(array1,array2,array3)

