import random

def printArr(arr):
    for r in range(len(arr)):
        for c in range(len(arr[0])):
            print(arr[r][c], end = '')
        print()

def printArr(arr):
    for r in range(3):
        print('', arr[r][0], '|', arr[r][1], '|', arr[r][2])
        if r != 2:
            print('---|---|---')

def isWin(arr, turn):
    judge = False
    for i in range(3):
        if arr[i][0] == arr[i][1] == arr[i][2] == turn:
            judge = True
        if arr[0][i] == arr[1][i] == arr[2][i] == turn:
            judge = True
    if arr[0][0] == arr[1][1] == arr[2][2] == turn or arr[0][2] == arr[1][1] == arr[2][0] == turn:
        judge = True
    return judge


arr = [[' ']*3 for _ in range(3)]
printArr(arr)

while True:
    x = int(input('다음 수의 x좌표를 입력하시오: '))
    y = int(input('다음 수의 y좌표를 입력하시오: '))
    if arr[x][y] != " ":
        print('잘못된 위치입니다.')
        continue
    else:
        arr[x][y] = 'X'
    while True:
        ai_x = random.randrange(0, 3)
        ai_y = random.randrange(0, 3)
        if arr[ai_x][ai_y] == " ":
            arr[ai_x][ai_y] = 'O'
            break
        else:
            continue
    printArr(arr)
    if isWin(arr, 'X'):
        print('당신이 이겼습니다.')
        break
    if isWin(arr, 'O'):
        print('당신이 졌습니다.')
        break
    
    
