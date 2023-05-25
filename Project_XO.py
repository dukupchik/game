# Крестики-нолики
s = [["_","_","_"],["_","_","_"],["_","_","_"]]
possible_moves = [11, 12, 13, 21, 22, 23, 31, 32, 33]

def pole():
    print(*s[0])
    print(*s[1])
    print(*s[2])

def move(gamer):
    while True:
        print('Ходит', gamer, '. Введите коррдинаты', possible_moves, ': ')
        n = int(input())
        if n in possible_moves:
            del possible_moves[possible_moves.index(n)]
            s[n//10-1][n%10-1] = gamer
            pole()
            break
        else:
            print('Неверные координаты, попробуйте снова')

def check_pole():
    win = False
    for i in range(3):
        if (s[i][0] == s[i][1] == s[i][2] != '_') or (s[0][i] == s[1][i] == s[2][i] != '_'):
            win = True
    if (s[0][0] == s[1][1] == s[2][2] != '_') or (s[2][0] == s[1][1] == s[0][2] != '_'):
        win = True
    return win

print('Добро пожаловать в игру Крестики-Нолики! Давай сыграем!')

while True:
    if possible_moves == []:
            print('Игра окончена! Победила дружба! :)')
            break
    move('X')
    if check_pole():
        print('Поздравляем! Игрок Х победил!')
        break
    move('O')
    if check_pole():
        print('Поздравляем! Игрок О победил!')
        break




